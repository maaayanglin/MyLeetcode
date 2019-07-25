# 执行用时 :56 ms, 在所有 Python3 提交中击败了79.51%的用户
# 内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.12%的用户

# 思路：
# 要找到下一个排列数，需要从给定数据的右边开始分析，因为一串数字的右边是低位，能更方便快速的确定下一个排列数。
# 首先我们都知道一串数字若从左往右是按降序排列的，则该串数字是其内部数字随机排列能构成的值最大的排列。假如我们再给一个数字tmp放到该降序排列的数字串nums_sorted前，
# 可以分为两种情况：1、数字tmp的值大于降序数字串nums_sorted的最高位数字的值，则新构成的数字串仍然为降序数字串，若要找该数字串的下一个排列数则需要再往高位找
#                 2、数字tmp的值小于降序数字串nums_sorted的最高位数字的值，则新构成的数字串的下一个排列数与更高位数字无关，可以继续往下讨论：
# 此时我们截取从tmp位开始的右边的数字串命名为nums_main，下一个排列数必定满足：
#                 1、下一个排列数的最左侧即最高位数字值必定大于数字tmp，
#                 2、下一个排列数的最高位的右边的数字串排列是升序排列的
# 同时我们也知道当截断后nums_main的最高位的右边的数字串排列是降序的，基于此以及上述第一点我们需要从nums_main的右边开始遍历，找到第一个大于tmp的数字target
# 然后将target与tmp交换即能满足第一条规定。当然，交换后除最高位外的数字串仍然是降序的。（小于tmp的也小于target，大于target的也大于tmp，两者交换不影响有序性）
# 最后将nms_main除最高位外的数字串进行翻转，从降序变成升序，即满足上述条件二。此时的整个排列数即为下一个排列数。

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ridx = n - 1
        while ridx > 0 and nums[ridx-1] >= nums[ridx]:
            ridx -= 1
        if ridx == 0:
            nums.reverse()
            return 
        else:
            first_idx = ridx - 1
            rridx = n - 1
            while nums[first_idx] >= nums[rridx]:
                rridx -= 1
            second_idx = rridx
            nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
            
            lidx = ridx
            ridx = n - 1
            while lidx <= ridx:
                nums[lidx], nums[ridx] = nums[ridx], nums[lidx]
                ridx -= 1
                lidx += 1
            return 
