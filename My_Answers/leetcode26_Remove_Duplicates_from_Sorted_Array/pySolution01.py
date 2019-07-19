# 执行用时 :60 ms, 在所有 Python3 提交中击败了99.44%的用户
# 内存消耗 :14.8 MB, 在所有 Python3 提交中击败了36.01%的用户

# 思路：顺序遍历。用count表示不重复元素下标。当遍历的元素重复时count不变，不重复时将该元素赋值给count当前位置，后count+1后移。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for n, ele in enumerate(nums):
            if n > 0 and ele == nums[n-1]:
                pass
            else:
                nums[count] = ele
                count += 1
        return count+1
