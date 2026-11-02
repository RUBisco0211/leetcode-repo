"""leetcode.cn 访问层：从 Edge 浏览器读取登录 cookie、GraphQL 查询、HTTP 请求。

不依赖 leetgo（leetgo 1.5.2 对 leetcode.cn 的远程测试接口已失效），
只依赖 macOS 自带的 security / openssl 命令。
"""

import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import tempfile

SITE = "https://leetcode.cn"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
EDGE_COOKIE_DB = "~/Library/Application Support/Microsoft Edge/Default/Cookies"
KEYCHAIN_SERVICE = "Microsoft Edge Safe Storage"


class LeetCodeError(RuntimeError):
    pass


def _edge_aes_key():
    p = subprocess.run(
        ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
        capture_output=True, text=True,
    )
    pwd = p.stdout.strip()
    if not pwd:
        raise LeetCodeError(
            "无法从 Keychain 读取 Edge 主密钥（可能需要授权）。\n"
            "可在 系统设置 > 隐私与安全性 > 完全磁盘访问权限 中放行终端，或改用其他登录方式。"
        )
    return hashlib.pbkdf2_hmac("sha1", pwd.encode(), b"saltysalt", 1003, 16).hex()


def _decrypt(enc, key):
    if enc[:3] not in (b"v10", b"v11"):
        return enc.decode("utf-8", "ignore")
    p = subprocess.run(
        ["openssl", "enc", "-aes-128-cbc", "-d", "-K", key, "-iv", "20" * 16],
        input=enc[3:], capture_output=True,
    )
    out = p.stdout
    if len(out) > 32:          # Chrome/Edge >= v80 前置 32 字节 domain hash
        out = out[32:]
    return out.decode("utf-8", "ignore")


def cookie_header(db_path=EDGE_COOKIE_DB):
    """返回 leetcode.cn 的 Cookie 请求头字符串。"""
    src = os.path.expanduser(db_path)
    if not os.path.exists(src):
        raise LeetCodeError(f"找不到浏览器 cookie 数据库：{src}")
    key = _edge_aes_key()
    tmp = tempfile.mktemp(suffix=".db")
    shutil.copy(src, tmp)                      # 直接读会被锁
    try:
        con = sqlite3.connect(tmp)
        rows = con.execute(
            "select name, encrypted_value from cookies "
            "where host_key like '%leetcode%' and expires_utc > 13380000000000000"
        ).fetchall()
        con.close()
    finally:
        os.remove(tmp)
    jar = {}
    for name, enc in rows:
        jar.setdefault(name, _decrypt(enc, key))
    if "LEETCODE_SESSION" not in jar:
        raise LeetCodeError("Edge 里没有 leetcode.cn 的登录状态，请先在 Edge 登录 leetcode.cn")
    return "; ".join(f"{k}={v}" for k, v in jar.items()), jar.get("csrftoken", "")


class Client:
    def __init__(self):
        self.cookie, self.csrf = cookie_header()

    def _curl(self, url, data=None, referer=None, content_type="application/json", timeout=60):
        cmd = [
            "curl", "-s", "-m", str(timeout), "-X", "POST" if data is not None else "GET", url,
            "-H", f"cookie: {self.cookie}",
            "-H", f"x-csrftoken: {self.csrf}",
            "-H", f"origin: {SITE}",
            "-H", f"referer: {referer or SITE + '/'}",
            "-H", f"content-type: {content_type}",
            "-A", UA,
        ]
        if data is not None:
            cmd += ["--data-raw", data]
        p = subprocess.run(cmd, capture_output=True, text=True)
        try:
            return json.loads(p.stdout)
        except Exception:
            raise LeetCodeError(f"非 JSON 响应：{p.stdout[:300]!r} {p.stderr[:200]!r}")

    def gql(self, query, variables=None):
        payload = json.dumps({"query": query, "variables": variables or {}})
        return self._curl(SITE + "/graphql", payload, referer=SITE + "/")

    def question_id(self, slug):
        r = self.gql("query($s:String!){ question(titleSlug:$s){ questionId titleSlug } }", {"s": slug})
        q = (r.get("data") or {}).get("question")
        if not q:
            raise LeetCodeError(f"查不到题目 slug={slug}: {json.dumps(r, ensure_ascii=False)[:200]}")
        return q["questionId"]

    def submit(self, slug, question_id, lang, code):
        payload = json.dumps({
            "lang": lang,
            "question_id": str(question_id),
            "typed_code": code,
            "judge_type": "large",
        })
        return self._curl(f"{SITE}/problems/{slug}/submit/", payload,
                          referer=f"{SITE}/problems/{slug}/")

    def check(self, submission_id):
        return self._curl(f"{SITE}/submissions/detail/{submission_id}/check/",
                          referer=f"{SITE}/submissions/detail/{submission_id}/")
