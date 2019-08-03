# 执行用时 :128 ms, 在所有 Python3 提交中击败了17.44%的用户
# 内存消耗 :15 MB, 在所有 Python3 提交中击败了5.30%的用户

#思路：二分法：一次二分找出第一个等于target的数，第二次二分时开始low的直接以第一次的结果为起点，起到节省作用，找出最后一个等于target的数。

class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if not nums:
            return [-1, -1]
        low = 0
        length = len(nums) - 1
        high = length
        res = []
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        if low <= length and nums[low] == target:
            res.append(low)
        else: #  若第一次搜索无结果直接返回[-1, -1]
            return [-1, -1]
        high = length
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid < length and target == nums[mid] and target < nums[mid+1]:
                res.append(mid)
                return res
            elif target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        res.append(length)
        return res
