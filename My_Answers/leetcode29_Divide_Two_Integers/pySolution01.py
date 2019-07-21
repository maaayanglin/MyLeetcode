# 执行用时 :44 ms, 在所有 Python3 提交中击败了95.88%的用户
# 内存消耗 :14 MB, 在所有 Python3 提交中击败了5.30%的用户

# 思路，利用竖式相除法的思想，通过二进制移位相减的技巧求得商

MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    def divide(self, dividend, divisor):
        vector = True if (dividend > 0) ^ (divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        ret = 0
        while count:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                ret += 1 << count
                dividend -= divisor
        if ret>MAX_INT or ret < MIN_INT:
            return MAX_INT if vector else MIN_INT
        return ret if vector else -ret
