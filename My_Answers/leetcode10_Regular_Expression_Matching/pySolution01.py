class Solution(object):
# 暴力法：
# 执行用时 :2128 ms, 在所有 Python3 提交中击败了8.71%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了91.26%的用户
    # def isMatch(self, text, pattern):
    #     if not pattern:
    #         return not text
    #     first_match = bool(text) and pattern[0] in (text[0], '.')
    #     if len(pattern)>=2 and pattern[1]=='*':
    #         return self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern)
    #     else:
    #         return first_match and self.isMatch(text[1:], pattern[1:])
    
# 动态规划优化
# 执行用时 :56 ms, 在所有 Python3 提交中击败了98.57%的用户
# 内存消耗 :13.4 MB, 在所有 Python3 提交中击败了23.19%的用户

    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(pattern):
                return i == len(text)
            first = i < len(text) and pattern[j] in {'.', text[i]}
            if j < len(pattern)-1 and pattern[j+1] == '*':
                ans = dp(i, j+2) or first and dp(i+1, j)
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)
