# 执行用时 :152 ms, 在所有 Python3 提交中击败了59.17%的用户
# 内存消耗 :13 MB, 在所有 Python3 提交中击败了96.64%的用户

class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        min_delta = float('inf')
        clo_num = nums[0]
        for i, a in enumerate(nums[:-2]):
            lidx = i+1
            ridx = length - 1
            while lidx < ridx:
                if i > 0 and nums[lidx] == nums[lidx-1] and nums[i] == nums[i-1]:
                    lidx += 1
                    continue
                elif ridx+1 < length-2 and nums[ridx] == nums[ridx+1]:
                    ridx -= 1
                    continue
                tmp = a + nums[lidx] + nums[ridx]
                delta = abs(target - tmp)
                if delta < min_delta:
                    min_delta = delta
                    clo_num = tmp
                if tmp > target:
                    ridx -= 1
                elif tmp < target:
                    lidx += 1
                else:
                    return tmp
            if a > target:
                break
        return clo_num


if __name__ == '__main__':
    t = [1,2,4,8,16,32,64,128]
    obj = Solution()
    res = obj.threeSumClosest(t, 82)
    print(res)
