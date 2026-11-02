# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/find-median-from-data-stream/

from typing import *
from leetgo_py import *

# @lc code=begin

class MedianFinder:

    def __init__(self):
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MedianFinder()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addNum(num)
                output.append("null")
            case "findMedian":
                ans = serialize(obj.findMedian())
                output.append(ans)

    print("\noutput:", join_array(output))
