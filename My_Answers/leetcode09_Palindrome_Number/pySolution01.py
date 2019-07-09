# 执行用时 :92 ms, 在所有 Python3 提交中击败了90.14%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了91.76%的用户

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            if x<0:
                return False
            rev = int(''.join(list(reversed(str(x)))))
            if rev == x:
                return True
            else:
                return False
        except:
            return False
