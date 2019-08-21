#执行用时 :52 ms, 在所有 Python3 提交中击败了82.57%的用户
#内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.00%的用户

# 思路：由目标的前项计算目标项：顺序遍历前项的元素同时进行计数即可推导出后项

class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        while n>1:
            count, tmp = 1, ''
            for idx in range(len(res) - 1):
                if res[idx] == res[idx+1]:
                    count += 1
                else:
                    tmp += str(count)
                    tmp += res[idx]
                    count = 1
            tmp += str(count)
            tmp += res[-1]
            res = tmp
            n -= 1
        return res
