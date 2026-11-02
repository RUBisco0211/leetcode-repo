# LeetCode 刷题

个人刷题仓库（[leetcode.cn](https://leetcode.cn)），含全部历史提交，不限于热题 100。进度见 [HOT100.md](HOT100.md)，历史归档见 [IMPORTED.md](IMPORTED.md)。

## 依赖

- [pi](https://github.com/earendil-works/pi-coding-agent) —— 用来刷题的 coding agent
- [leetgo](https://github.com/j178/leetgo) —— 生成题目脚手架（`brew install leetgo`）
- Python venv：`python/.venv`，依赖见 `python/requirements.txt`

## 如何提交

```bash
scripts/lc_submit.py python/0283.move-zeroes
```

pi 在 `solution.py` 的 `@lc code=begin` ~ `@lc code=end` 之间写题解后执行上面命令即可。

提交成功后：

- 代码提交到 leetcode.cn 跑完全部用例并 AC
- AC 代码归档到 `python/<题号>.<slug>/solutions/python3/<题号>.<slug>-<submission_id>.py`（不覆盖已有文件）
- `solution.py` 自动还原为 stub（脚手架状态）
- 自动 `git commit`，消息形如 `solve(283.move-zeroes): AC submission <id>`

常用参数：`--dry-run`（只看不提交）、`--no-commit`（归档但不 commit）。
