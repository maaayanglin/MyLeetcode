# 执行用时 :64 ms, 在所有 Python3 提交中击败了25.61%的用户
# 内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.73%的用户

# 思路：二分查找
# 一：目标值target>中间值nums[mid]，需要分析要取左半序列还是右半序列：
#       1:大序列存在且中间值nums[mid]位于大序列内，即nums[mid]>nums[lidx]，由target>nums[mid]>nums[lidx]可知此时目标值target必定属于大序列内
# 的元素，此时目标元素位于右半序列。二分时指针移动代码：lidx = mid + 1
#       2:中间值nums[mid]位于小序列内：
#          i:大序列不存在：直接取右半序列，二分指针移动代码：lidx = mid + 1
#          ii:大序列存在：
#               ①:目标值属于大序列：大序列必定在小序列左边，故目标元素位于左半序列。二分指针移动代码：ridx = mid - 1
#               ②:目标值属于小序列：由target>nums[mid]可知需要取右半序列，二分指针移动代码：lidx = mid + 1
#               ③:目标值大于小序列最大值且小于大序列最小值时不在序列内：return -1
# 二：目标值target<中间值nums[mid]
#       分析类似一：略
# 三：目标值target==中间值nums[mid]：return mid

# 时间复杂度：O(logn)
# 空间复杂度：O(1)

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        lidx, ridx = 0, len(nums) - 1
        while lidx <= ridx:
            mid = lidx + ((ridx - lidx) >> 1)  # 等价于(lidx + ridx) // 2 
            # 目标值大于中间值
            if target > nums[mid]:
                # 大序列存在，且中间值处于大序列(此时目标值必定属于大序列)，
                if (nums[ridx] < nums[lidx]) and (nums[mid] > nums[lidx]):
                    lidx = mid + 1
                # 大序列不存在，或大序列存在且中间值处于小序列
                else:
                    if nums[lidx] < nums[ridx]:  # 大序列不存在
                        lidx = mid + 1
                    else:
                        if target <= nums[ridx]:  # 目标值属于小序列
                            lidx = mid + 1
                        elif target >= nums[lidx]:  # 目标值属于大序列
                            ridx = mid - 1
                        else:
                            return -1

            # 目标值小于中间值
            elif target < nums[mid]:
                # 大序列存在，且中间值属于小序列(此时目标值必定属于小序列)
                if (nums[ridx] < nums[lidx]) and (nums[mid] < nums[ridx]):
                    ridx = mid - 1
                # 大序列不存在，或者大序列存在且中间值处于大序列
                else:
                    if nums[lidx] < nums[ridx]:  # 大序列不存在
                        ridx = mid - 1
                    else:
                        if target >= nums[lidx]:  # 目标值属于大序列
                            ridx = mid - 1
                        elif target <= nums[ridx]:  # 目标值属于小序列
                            lidx = mid + 1
                        else:
                            return -1

            # 目标值等于中间值
            else:
                return mid
        return -1  # 检索完毕仍然没被return，表示该元素不在列表内，return -1
