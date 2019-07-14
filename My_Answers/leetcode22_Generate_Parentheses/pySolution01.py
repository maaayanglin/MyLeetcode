# 执行用时 :48 ms, 在所有 Python3 提交中击败了95.94%的用户
# 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了83.02%的用户

# 思路：采用回溯的方法，通过递归实现。当左括号未放置数非0且小于等于右括号未放置数时放置左括号满足匹配，
#                                  当右括号未放置数非0且左括号未匹配数小于右括号未匹配数时放置右括号亦可满足匹配。
#                                  当左括号和右括号未放置数均为0时结束递归

class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.helper('', n, n)
        return self.res
    
    def helper(self, pre_res, left, right):
        if left + right == 0:
            self.res.append(pre_res)
            return
        if left and left <= right:            
            self.helper(pre_res+'(', left-1, right)
        if right and left < right:
            self.helper(pre_res+')', left, right-1)
            
