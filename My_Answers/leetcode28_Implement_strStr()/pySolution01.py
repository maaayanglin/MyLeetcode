# 执行用时 :36 ms, 在所有 Python3 提交中击败了99.39%的用户
# 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了86.08%的用户

# 直接利用python字符串方法find()，没有什么技巧。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
# 常规写法：
# 执行用时 :44 ms, 在所有 Python3 提交中击败了93.90%的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了51.10%的用户

# 遍历字符串，利用切片判断是否与needle相等即可
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
