# 执行用时 :76 ms, 在所有 Python3 提交中击败了84.40%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了94.74%的用户

class Solution:
    # def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        roman = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        ret = ''
        divisor = 1000
        while num>0:
            count = num // divisor
            num -= count * divisor
            if count == 9:
                ret += roman[divisor] + roman[divisor*10]
            elif count >= 5:
                tmp = roman[divisor*5] + roman[divisor] * int(count-5)
                ret += tmp
            elif count == 4:
                ret += roman[divisor] + roman[divisor*5]
            else:
                ret += roman[divisor]*int(count)
            divisor /= 10
        return ret
