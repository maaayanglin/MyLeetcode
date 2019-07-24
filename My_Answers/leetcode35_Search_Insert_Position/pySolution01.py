# 执行用时 :96 ms, 在所有 Python3 提交中击败了5.60%的用户
# 内存消耗 :14.2 MB, 在所有 Python3 提交中击败了5.47%的用户

# easy but slow !
# 思路： 等价于在列表中查找第一个值大于或等于给定值的元素下标，没有则相当于在列表最后插入元素的位置

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)  # 向下圆整
            if nums[mid] >= target:
                if (mid == 0) or (nums[mid-1] < target):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return len(nums)
