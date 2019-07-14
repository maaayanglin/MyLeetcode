# 执行用时 :48 ms, 在所有 Python3 提交中击败了87.79%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了72.53%的用户

# 利用栈后进先出的思想，遇到左括号就压入栈内，遇到右括号则且与栈顶左括号配对则弹出栈顶。程序运行完栈为空则正确。

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        d = {'}': '{', ')': '(', ']': '['}
        check_left = []
        for string in s:
            if string in ['(', '[', '{']:
                check_left.append(string)
            if string in ['}', ')', ']']:
                if check_left and check_left[-1] == d[string]:
                    check_left.pop()
                else:
                    return False
        return not check_left
            
