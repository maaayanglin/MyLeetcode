# 执行用时 :72 ms, 在所有 Python3 提交中击败了96.13%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了96.21%的用户

# 思路，构建罗马数字-整数的映射字典，从左往右遍历罗马字符串，比较当前罗马数值和下一罗马数值的大小即可。

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        ret, tag = 0, 0
        for index, ro in enumerate(s):
            if tag:
                tag = 0
                continue
            if len(s)-1>index:
                if roman[ro] >= roman[s[index+1]]:
                    ret += roman[ro]
                    tag = 0
                elif roman[ro] < roman[s[index+1]]:
                    tmp = roman[s[index+1]] - roman[ro]
                    ret += tmp
                    tag = 1
            else:
                ret += roman[ro]
        return ret
