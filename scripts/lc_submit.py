#!/usr/bin/env python3
"""提交 leetcode.cn 题目 → 在线跑全部用例 → AC 后归档到 solutions/<lang>/ 并还原 stub → git commit。

用法:
    scripts/lc_submit.py python/0001.two-sum
    scripts/lc_submit.py python/0001.two-sum/solution.py
    scripts/lc_submit.py python/0001.two-sum --dry-run     # 只看将提交的代码，不真的提交
    scripts/lc_submit.py python/0001.two-sum --no-commit   # 归档+还原，但不 git commit
    scripts/lc_submit.py python/0001.two-sum --keep-stub   # 不还原 solution.py

约定:
    * 提交的是 solution.py 中 `@lc code=begin` ~ `@lc code=end` 之间的代码（去除 leetgo 脚手架）
    * AC 后归档为 solutions/<lang>/<basename>-<submission_id>.<ext>，绝不覆盖已有文件
    * 之后把 solution.py 用 git restore 还原为基线 stub
"""

import argparse
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lc_common import Client, LeetCodeError, SITE  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUS = {
    10: ("Accepted", "✅"),
    11: ("Wrong Answer", "✘"),
    12: ("Memory Limit Exceeded", "✘"),
    13: ("Output Limit Exceeded", "✘"),
    14: ("Time Limit Exceeded", "✘"),
    15: ("Runtime Error", "✘"),
    16: ("Internal Error", "✘"),
    20: ("Compile Error", "✘"),
    21: ("Unknown Error", "✘"),
    30: ("Timeout", "✘"),
}

def label(qid, slug):
    return f"{qid}.{slug}" if qid.isdigit() else f"{qid} {slug}"


BASE_NAME = {"python3": ("solution", "py"), "python": ("solution", "py"),
             "java": ("Solution", "java"), "cpp": ("solution", "cpp"), "c": ("solution", "c"),
             "golang": ("solution", "go"), "rust": ("solution", "rs"),
             "typescript": ("solution", "ts"), "javascript": ("solution", "js"),
             "mysql": ("solution", "sql"), "csharp": ("Solution", "cs"), "kotlin": ("Solution", "kt")}

C_STYLE = {"java", "cpp", "c", "golang", "rust", "typescript", "javascript", "csharp", "kotlin"}

MARK_RE = re.compile(r"^[^\w\s]{0,3}\s*@lc code=(begin|end)", re.M)


def comment_prefix(lang):
    if lang in C_STYLE:
        return "//"
    if lang == "mysql":
        return "--"
    return "#"


def extract_code(text, lang):
    """取出真正要提交的解答代码：优先 @lc 标记之间，否则剔除 leetgo 脚手架。"""
    lines = text.split("\n")
    begin = end = None
    for i, ln in enumerate(lines):
        m = MARK_RE.match(ln.strip())
        if not m:
            continue
        if m.group(1) == "begin":
            begin = i
        elif m.group(1) == "end" and begin is not None:
            end = i
            break
    if begin is not None and end is not None:
        body = lines[begin + 1:end]
    else:
        body = []
        for ln in lines:
            if ln.strip().startswith("if __name__") and "__main__" in ln:
                break
            if re.match(r"^\s*from leetgo_py import", ln):
                continue
            body.append(ln)
    code = "\n".join(body).strip("\n")
    if not code.strip():
        raise SystemExit("✘ solution.py 里没有找到解答代码")
    return code


def parse_problem(path):
    """解析题目标识符。优先读 question.md 里的题目链接（最可靠），否则回退到目录名 <id>.<slug>。"""
    p = os.path.abspath(path)
    if os.path.isfile(p):
        p = os.path.dirname(p)
    p = p.rstrip("/")
    name = os.path.basename(p)
    qid = name.split(".", 1)[0] if "." in name else name
    slug = None

    qm = os.path.join(p, "question.md")
    if os.path.exists(qm):
        text = open(qm, encoding="utf-8").read()
        m = re.search(r"https?://leetcode\.cn/problems/([A-Za-z0-9_\-]+)/", text)
        if m:
            slug = m.group(1)
        h = re.search(r"^#\s*\[([^\]]+)\]", text, re.M)
        if h:
            qid = h.group(1).split(". ", 1)[0].strip()   # "面试题 02.07. 链表相交" -> "面试题 02.07"
    if not slug and "." in name:
        slug = name.split(".", 1)[1]
    if not slug:
        raise SystemExit(f"✘ 无法从 {p} 解析题目 slug（目录名 '{name}'，且 question.md 无题目链接）")
    return p, qid, slug


def poll(client, sid, timeout=300):
    t0 = time.time()
    while time.time() - t0 < timeout:
        r = client.check(sid)
        state = r.get("state")
        if state not in ("PENDING", "STARTED", None):
            return r
        if "超出访问限制" in str(r.get("error") or "") or "Too Many" in str(r):
            print("   ⏳ 判题接口限流，等待后继续…")
            time.sleep(20)
        else:
            time.sleep(1.5)
    raise SystemExit(f"✘ 轮询超时（{timeout}s），submission {sid} 结果请到网页查看")


def report_failure(r):
    code = r.get("status_code")
    name, _ = STATUS.get(code, (r.get("status_msg") or "Unknown", "✘"))
    total = r.get("total_testcases")
    correct = r.get("total_correct")
    print(f"\n✘ {name}  ({correct}/{total} 用例通过)")

    if r.get("full_compile_error") or r.get("compile_error"):
        print("\n— 编译错误 —")
        print((r.get("full_compile_error") or r.get("compile_error")).strip()[:4000])
    if r.get("full_runtime_error") or r.get("runtime_error"):
        print("\n— 运行时错误 —")
        print((r.get("full_runtime_error") or r.get("runtime_error")).strip()[:4000])
        if r.get("last_testcase"):
            print(f"\n出错用例: {r['last_testcase']}")

    if r.get("input_formatted") or r.get("input"):
        print("\n— 第一个失败的用例 —")
        print(f"  输入:   {r.get('input_formatted') or str(r.get('input')).replace(chr(10), ' | ')}")
        if r.get("expected_output") is not None:
            print(f"  期望:   {r['expected_output']}")
        if r.get("code_output") is not None:
            print(f"  实际:   {r['code_output']}")

    bm = r.get("compare_result") or ""
    fails = [i + 1 for i, c in enumerate(bm) if c == "0"]
    if fails:
        head = ", ".join(f"#{i}" for i in fails[:12])
        more = f" … 共 {len(fails)} 个" if len(fails) > 12 else ""
        print(f"\n— 失败用例序号: {head}{more}")


def archive(dirpath, lang, code, sid, slug, qid, r):
    base, ext = BASE_NAME.get(lang, ("solution", lang))
    outdir = os.path.join(dirpath, "solutions", lang)
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"{base}-{sid}.{ext}")
    if os.path.exists(path):
        raise SystemExit(f"✘ 归档文件已存在，拒绝覆盖: {path}")
    cp = comment_prefix(lang)
    when = time.strftime("%Y-%m-%d")
    header = "\n".join([
        f"{cp} leetcode.cn/problems/{slug}/  ({qid})",
        f"{cp} submission {sid}  accepted {when}  "
        f"runtime {r.get('status_runtime')}  memory {int(r.get('memory') or 0) / 1e6:.1f} MB",
        "", ""])
    with open(path, "w") as f:
        f.write(header + code.rstrip() + "\n")
    return path


HOT100_PROMPT = """你在仓库 {repo} 里工作，只允许改动 {hot100} 这一个文件。

任务：这道题刚刚被 AC 了，请把它在热题 100 清单里标记为完成。
- 题号：{qid}
- slug：`{slug}`

具体做两件事，其它内容一个字都不要改（表格、其它题目行、说明文字保持原样）：
1. 在 {hot100} 里找到 slug 为 `{slug}`（题号 {qid}）的那一行，它现在形如
   `- [ ]  283. Move Zeroes ...`，把方括号里的空格改成 `x`。
2. 文件顶部的进度行形如 `进度：**71/100 已 AC**（`~` 尝试未通过 3，空白未开始 26）。`，
   按你改动后的真实情况更新其中三个数字：已 AC 数 / 总数 100、`~` 的题数、空白未开始的题数
   （三个数字相加应等于总题数），括号内的措辞格式保持不变。

完成后只回复一行：改动的行数和你更新的进度数字。"""


def update_hot100(qid, slug, timeout=240):
    """交给本地 pi agent 更新 HOT100.md（不做正则解析）。返回 True 表示文件有变化。"""
    hot100 = os.path.join(REPO, "HOT100.md")
    if not os.path.exists(hot100):
        print("⚠ 没有 HOT100.md，跳过清单更新")
        return False
    if f"`{slug}`" not in open(hot100).read():
        print(f"● {slug} 不在热题100 清单里，跳过清单更新")
        return False

    before = open(hot100).read()
    prompt = HOT100_PROMPT.format(repo=REPO, hot100="HOT100.md", qid=qid, slug=slug)
    print("● 调用 pi agent 更新 HOT100.md …")
    try:
        p = subprocess.run(
            ["pi", "-p", "--no-session", "--tools", "read,edit", prompt],
            cwd=REPO, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        print(f"⚠ pi agent 超时（{timeout}s），跳过清单更新")
        return False
    out = (p.stdout or "").strip().splitlines()
    if out:
        print("   pi: " + out[-1][:200])
    after = open(hot100).read()
    if after == before:
        print("⚠ HOT100.md 没有被修改（agent 未生效）")
        return False
    return True


def restore_stub(dirpath, stub, slug):
    rel = os.path.relpath(stub, REPO)
    cur = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=REPO,
                         capture_output=True, text=True)
    if cur.returncode != 0:
        print(f"⚠ {rel} 不在 git 基线里，改用 leetgo 重新生成 stub")
        subprocess.run(["leetgo", "-y", "pick", slug, "--skip-editor"], cwd=REPO,
                       stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        return
    subprocess.run(["git", "restore", "--source=HEAD", "--", rel], cwd=REPO, check=True)
    print(f"↩ 已还原 {rel} 为初始 stub")


def git_commit(dirpath, qid, slug, sid, lang, archive_path, r, hot100_updated=False):
    rel_dir = os.path.relpath(dirpath, REPO)
    rel_archive = os.path.relpath(archive_path, REPO)
    subprocess.run(["git", "add", "--", rel_dir], cwd=REPO, check=True)
    if hot100_updated:
        subprocess.run(["git", "add", "--", "HOT100.md"], cwd=REPO, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO)
    if diff.returncode == 0:
        print("⚠ 暂存区没有变化，跳过 commit")
        return
    total = f"{r.get('total_correct')}/{r.get('total_testcases')}"
    msg = (f"solve({label(qid, slug)}): AC submission {sid}\n\n"
           f"- 题目标识: {qid} / {slug}\n"
           f"- submission: {sid}\n"
           f"- 语言: {lang}\n"
           f"- 归档: {rel_archive}\n"
           f"- 结果: {total} 通过, {r.get('status_runtime')}, "
           f"{int(r.get('memory') or 0) / 1e6:.1f} MB\n"
           + ("- HOT100.md: 已标记完成\n" if hot100_updated else ""))
    subprocess.run(["git", "commit", "-q", "-m", msg], cwd=REPO, check=True)
    print(f"📝 已提交: solve({label(qid, slug)}): AC submission {sid}")


def main():
    ap = argparse.ArgumentParser(description="提交 leetcode.cn 题目并在 AC 后归档题解")
    ap.add_argument("path", help="题目目录（或其中的 solution.py）相对路径，如 python/0001.two-sum")
    ap.add_argument("-l", "--lang", default="python3", help="提交语言（默认 python3）")
    ap.add_argument("--dry-run", action="store_true", help="只打印将提交的代码")
    ap.add_argument("--no-commit", action="store_true", help="AC 后不执行 git commit")
    ap.add_argument("--keep-stub", action="store_true", help="AC 后不还原 solution.py")
    ap.add_argument("--no-hot100", action="store_true", help="AC 后不更新 HOT100.md")
    args = ap.parse_args()

    dirpath, qid, slug = parse_problem(args.path)
    stub = os.path.join(dirpath, "solution.py")
    if not os.path.exists(stub):
        stub = os.path.join(dirpath, BASE_NAME.get(args.lang, ("solution", "py"))[0] +
                            "." + BASE_NAME.get(args.lang, ("solution", "py"))[1])
    if not os.path.exists(stub):
        raise SystemExit(f"✘ 找不到解答文件: {stub}")

    code = extract_code(open(stub).read(), args.lang)
    print(f"● {label(qid, slug)}  [{args.lang}]  {len(code.splitlines())} 行 / {len(code)} 字符")
    if args.dry_run:
        print("-" * 60)
        print(code)
        return 0

    client = Client()
    question_id = client.question_id(slug)
    print(f"● question_id={question_id}，提交中…")

    resp = client.submit(slug, question_id, args.lang, code)
    sid = resp.get("submission_id")
    if not sid:
        raise SystemExit(f"✘ 提交失败: {resp}")
    sid = str(sid)
    print(f"● submission {sid}，等待判题…")
    result = poll(client, sid)

    status_code = result.get("status_code")
    if status_code != 10:
        report_failure(result)
        print(f"\n详情: {SITE}/submissions/detail/{sid}/")
        return 1

    total = f"{result.get('total_correct')}/{result.get('total_testcases')}"
    print(f"\n✅ Accepted  {total} 用例  {result.get('status_runtime')}  "
          f"{int(result.get('memory') or 0) / 1e6:.1f} MB")

    path = archive(dirpath, args.lang, code, sid, slug, qid, result)
    print(f"💾 已归档 {os.path.relpath(path, REPO)}")

    if not args.keep_stub:
        restore_stub(dirpath, stub, slug)
    hot100_done = False
    if not args.no_hot100:
        hot100_done = update_hot100(qid, slug)
    if not args.no_commit:
        git_commit(dirpath, qid, slug, sid, args.lang, path, result, hot100_done)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except LeetCodeError as e:
        sys.exit(f"✘ {e}")
