# LeetCode 热题 100

个人刷题仓库，按 [LeetCode 热题 100](https://leetcode.cn/studyplan/top-100-liked/) 学习计划刷题（站点：[leetcode.cn](https://leetcode.cn)），语言以 Python 为主。

- 进度清单：见 [HOT100.md](HOT100.md)
- 历史 AC 归档索引：见 [IMPORTED.md](IMPORTED.md)

## 目录结构

```
python/<题号>.<slug>/
├── question.md        # 题目描述（leetgo 生成）
├── solution.py        # 练习用 stub，只改 @lc code=begin ~ @lc code=end 之间
├── testcases.txt      # 测试用例
└── solutions/<lang>/  # AC 提交归档（按提交 ID 命名，不覆盖）
scripts/
├── lc_common.py       # leetcode.cn 访问层（读 Edge 登录 cookie + GraphQL）
└── lc_submit.py       # 提交 → 在线跑全部用例 → AC 后归档并 commit
```

## 依赖

| 依赖 | 说明 | 安装 |
|---|---|---|
| [leetgo](https://github.com/j178/leetgo) 1.5.2 | 生成题目脚手架 | `brew install leetgo` |
| Python 3.14 | 运行环境 | 已在 `python/.venv` 建好虚拟环境 |
| `leetgo_py` / `sortedcontainers` | 本地运行/测试用 | `pip install -r python/requirements.txt` |
| Microsoft Edge | leetcode.cn 登录态来源 | 需先在 Edge 登录 leetcode.cn |

> 提交脚本只依赖 macOS 自带的 `security` / `openssl`（读 Edge 的登录 cookie），不再依赖 leetgo 的远程接口。

安装 Python 依赖：

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 如何使用

### 拉取一道新题

```bash
leetgo pick 283        # 按题号生成，或交互式选择
```

生成后 `python/` 下会出现对应目录，在 `solution.py` 的 `@lc code=begin` ~ `@lc code=end` 之间写题解。

### 提交并归档

```bash
scripts/lc_submit.py python/0283.move-zeroes
```

脚本会：取出标记之间的代码 → 提交到 leetcode.cn 跑全部用例 → AC 后归档到 `solutions/<lang>/` → 把 `solution.py` 还原为 stub → 自动 `git commit`（消息形如 `solve(283.move-zeroes): AC submission <id>`）。

常用参数：

```bash
scripts/lc_submit.py python/0283.move-zeroes --dry-run    # 只看将提交的代码，不真提交
scripts/lc_submit.py python/0283.move-zeroes --no-commit  # 归档+还原，但不 git commit
```

## 如何提交（规范）

- 题解只写在 `solution.py` 的 `@lc code=begin` ~ `@lc code=end` 之间，不改动 leetgo 脚手架。
- 提交请走 `scripts/lc_submit.py`，它会自动归档并用规范消息 commit，无需手工 `git add/commit`。
- Commit 消息遵循 Conventional Commits：`solve(<题号>.<slug>): AC submission <id>`；其他改动用 `docs:` / `chore:` 等前缀。
- 每道题只保留一个 `solution.py`，历史 AC 都在 `solutions/` 下按提交 ID 单独归档。
