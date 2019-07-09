    
# 执行用时 :40 ms, 在所有 Python3 提交中击败了98.79%的用户
# 内存消耗 :13 MB, 在所有 Python3 提交中击败了98.71%的用户

# 思路，先取strs列表中最短字符串，再从左往右拿该字符串字符与其他串的同一索引位置的字符进行比较。
# 时间复杂度：O(minLen*n)，其中minLen为最短字符串长度，n为需要比较的字符串数
# 空间复杂度：O(1)，只需要常数量级的空间

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
