# LeetCode 刷题

个人刷题仓库（[leetcode.cn](https://leetcode.cn)）。HOT100 进度 [HOT100.md](HOT100.md)，历史归档 [IMPORTED.md](IMPORTED.md)。

## 依赖

- [pi](https://github.com/earendil-works/pi-coding-agent) —— `scripts/lc_submit.py` 提交成功后的文档维护
- [leetgo](https://github.com/j178/leetgo) —— 生成题目脚手架（`brew install leetgo`）

## 提交题解

```bash
scripts/lc_submit.py python/0283.move-zeroes
```

题解写在 `solution.py` 的 `@lc code=begin` ~ `@lc code=end` 之间，然后执行上面命令。

题解 AC 后自动归档并更新文档：

1. 归档代码到 `python/<题号>.<slug>/solutions/python3/solution-<submission_id>.py`
2. `solution.py` 还原为 stub 初始状态
3. 调用 pi 维护 `HOT100.md` 文档
4. `git commit`，消息形如 `solve(283.move-zeroes): AC submission <id>`

参数：`--dry-run`（只看将提交的代码）、`--no-commit`（归档但不 commit）、`--no-hot100`（不更新文档）。
