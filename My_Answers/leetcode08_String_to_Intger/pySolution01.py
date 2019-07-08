# 执行用时 :44 ms, 在所有 Python3 提交中击败了99.24%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了93.77%的用户
# 思路：首先清除首尾空字符，后区分正负来进行逐个字符匹配


INT_MAX = pow(2, 31) - 1
INT_MIN = pow(-2, 31)
class Solution:
    def myAtoi(self, str):
        s = str.strip()
        ret = 0
        sym = 1
        if s == '':
            return 0
        if s[0] == '-':
            sym = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        while True:
            try:
                l_pop = int(s[0])
                tmp = ret*10
                if sym == -1:
                    if tmp < INT_MIN:
                        return INT_MIN
                    elif tmp//-10 == INT_MIN//-10 and l_pop > 8:
                        return INT_MIN
                    ret = tmp - l_pop
                else:
                    if tmp > INT_MAX:
                        return INT_MAX
                    elif tmp//10 == INT_MAX//10 and l_pop > 7:
                        return INT_MAX
                    ret = tmp + l_pop
                s = s[1:]
            except:
                break
        return ret

if __name__ == '__main__':
    st = "-2147483649"
    o = Solution()
    rets = o.myAtoi(st)
    print(rets)
