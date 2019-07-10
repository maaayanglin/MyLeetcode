# 双指针法
# 首先对数组进行排序，排序后固定一个数nums[i]nums[i]，再使用左右指针指向i+1，len(nums)-1
# 时间复杂度：O(n^2)，n为数组长度
# 执行用时 :976 ms, 在所有 Python3 提交中击败了85.43%的用户
# 内存消耗 :16.2 MB, 在所有 Python3 提交中击败了99.52%的用户

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1  
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res
