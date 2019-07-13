# 执行用时 :44 ms, 在所有 Python3 提交中击败了93.19%的用户
# 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了42.69%的用户

# 思路：采用回溯的思想，利用递归来实现，将当前已组合的结果pre_str以及未进行组合的数字串digits传给递归函数，
# 线性条件：为digits为空时，表示所有数字都组合完毕，pre_str即为最终结果组合之一了，将其添加入返回结果的列表self.res
# 递归条件：digits不是空，表示还有数字待组合，取digits的第一个数字所映射的列表的所有元素进行组合，即将d[digits[0]]拼接到pre_str后形成新的组合。
#          再将新组合以及digits[1:]作为新递归的传入参数调用递归

class Solution:
    def __init__(self):
        self.d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        self.res = []

    def letterCombinations(self, digits):
        if not digits:
            return []
        self.helper('', digits)
        return self.res

    def helper(self, pre_str, digits):
        # 线性条件
        if not digits:
            self.res.append(pre_str)
            return pre_str
        # 继续递归
        for ele in self.d[digits[0]]:
            self.helper(pre_str+ele, digits[1:])
