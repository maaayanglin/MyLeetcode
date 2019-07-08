# 执行用时 :40 ms, 在所有 Python3 提交中击败了98.79%的用户
# 内存消耗 :13 MB, 在所有 Python3 提交中击败了98.71%的用户

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ret = ''
        min_str = min(strs, key=len)
        for index, char in enumerate(min_str):
            for s in strs:
                if s[index] != char:
                    return ret
            ret += char
        return ret
