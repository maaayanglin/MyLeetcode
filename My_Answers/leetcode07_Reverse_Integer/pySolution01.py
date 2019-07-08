##  comical sulutiono(*￣︶￣*)o
#执行用时 :44 ms, 在所有 Python3 提交中击败了97.04%的用户
#内存消耗 :13 MB, 在所有 Python3 提交中击败了99.05%的用户

class Solution:
    def reverse(self, x):
        sym = None
        if x<0:
            sym = str(x)[0]
            s_x = str(x)[1:]
        else:
            s_x = str(x)
        l = list(s_x)
        l.reverse()
        ret = int(''.join(l))
        if sym:
            ret = -ret
        if abs(ret)>(pow(2, 31)-1):
            ret = 0
        return ret
