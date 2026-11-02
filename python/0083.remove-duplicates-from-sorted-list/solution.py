# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)
    print("\noutput:", serialize(ans, "ListNode"))
