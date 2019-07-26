

# 思路：二分查找
# 2

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = nums[0], nums[-1]
        length = len(nums)
        lidx, ridx = 0, length - 1 
        while lidx <= ridx:
            mid = lidx + ((ridx - lidx) >> 1)
            # 目标值大于中间值
            if target > nums[mid]:
                # 中间值处于大序列(此时目标值必定属于大序列)，
                if nums[mid] > start:
                    lidx = mid + 1
                # 中间值处于小序列
                else:
                    pass
            # 目标值小于中间值
            elif target < nums[mid]:
                pass
            # 目标值等于中间值
            else:
                return nums[mid]
