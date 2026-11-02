# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/design-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyLinkedList:

    def __init__(self):
        

    def get(self, index: int) -> int:
        

    def addAtHead(self, val: int) -> None:
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyLinkedList()

    for i in range(1, len(ops)):
        match ops[i]:
            case "get":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(index))
                output.append(ans)
            case "addAtHead":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.addAtHead(val)
                output.append("null")
            case "addAtTail":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.addAtTail(val)
                output.append("null")
            case "addAtIndex":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.addAtIndex(index, val)
                output.append("null")
            case "deleteAtIndex":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                obj.deleteAtIndex(index)
                output.append("null")

    print("\noutput:", join_array(output))
