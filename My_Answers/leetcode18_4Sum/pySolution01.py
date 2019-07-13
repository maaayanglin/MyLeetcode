# 执行用时 :140 ms, 在所有 Python3 提交中击败了86.00%的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了38.07%的用户

# 思路：固定两个数，采用双指针法找到另外两个数，参考3Sum那道题目

class Solution(object):
    def fourSum(self, nums, target):
        ret = []
        length = len(nums)
        nums.sort()
        for idx, num in enumerate(nums[:-3]):
            if num+nums[idx+1]+nums[idx+2]+nums[idx+3]>target:
                break
            if num+nums[length-1]+nums[length-2]+nums[length-3]<target:
                continue
            if idx > 0 and num == nums[idx-1]:
                continue
            res = self.threeSum(nums[idx+1:], target-num)
            if res:
                for r in res:
                    r.insert(0, num)
                    ret.append(r)
        return ret

    def threeSum(self, nums, target):
        ret = []
        length = len(nums)
        for idx, num in enumerate(nums[:-2]):
            if num+nums[idx+1]+nums[idx+2]>target:
                break
            if num+nums[length-1]+nums[length-2]<target:
                continue
            if idx > 0 and nums[idx-1] == num:
                continue
            l_idx = idx + 1
            r_idx = len(nums) - 1
            while l_idx < r_idx:
                if nums[l_idx] == nums[l_idx-1] and num != nums[l_idx]:
                    l_idx += 1
                    continue
                elif length-1 > r_idx and nums[r_idx+1] == nums[r_idx]:
                    r_idx -= 1
                    continue
                tmp_sum = num + nums[l_idx] + nums[r_idx]
                if tmp_sum < target:
                    l_idx += 1
                elif tmp_sum > target:
                    r_idx -= 1
                else:
                    ret.append([num, nums[l_idx], nums[r_idx]])
                    l_idx += 1
                    r_idx -= 1
        return ret
