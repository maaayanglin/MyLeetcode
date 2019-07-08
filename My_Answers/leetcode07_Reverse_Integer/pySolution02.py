#  按照官方思路解题代码
#  执行用时 :48 ms, 在所有 Python3 提交中击败了92.67%的用户
#  内存消耗 :13.1 MB, 在所有 Python3 提交中击败了86.04%的用户


class Solution:
    def reverse(self, x):
        tmp = 0
        mod = -10 if x < 0 else 10
        while True:
            pop = x % mod
            tmp *= 10
            # print(f'tmp: {tmp} pop: {pop} ', end='')
            if tmp > MAX_INT or tmp < MIN_INT:
                return 0
            elif (tmp == MAX_INT and pop > 7) or (tmp == MIN_INT and pop < -8):
                return 0
            else:
                tmp += pop
            x = int(x/10)
            # print(f'x: {x}')
            if x == 0:
                break
        return tmp


if __name__ == '__main__':
    inte = -123
    o = Solution()
    ret = o.reverse(inte)
    print(ret)
