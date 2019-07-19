# 执行用时 :44 ms, 在所有 Python3 提交中击败了94.84%的用户
# 内存消耗 :12.8 MB, 在所有 Python3 提交中击败了99.31%的用户

# 思路：依次遍历，count为非指定元素存储的下标。遍历时若等于给定val则不做任何处理，否则将当前元素赋值给到nums下标为count的单元，count+1右移。

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for n, ele in enumerate(nums):
            if ele == val:
                pass
            else:
                nums[idx] = ele
                idx += 1
        return idx
