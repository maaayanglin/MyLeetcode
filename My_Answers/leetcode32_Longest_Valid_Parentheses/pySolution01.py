# 执行用时 :76 ms, 在所有 Python3 提交中击败了52.59%的用户
# 内存消耗 :14 MB, 在所有 Python3 提交中击败了16.92%的用户

# 思路：不使用栈的纯遍历方法。分别从左到右和从右到左共2次遍历，原理如下：
# 通过观察括号匹配情况，可以发现：
#     1、从左往右看，当左括号数>=右括号数，每来一个右括号定能满足匹配；当左括号数<右括号数，匹配必定中断，括号匹配长度也相应归0
#     2、从右往左看，当右括号数>=左括号数，每来一个左括号定能满足匹配；当右括号数<左括号数，匹配必定中断，括号匹配长度也相应归0
# 而题目要求的最长有效括号必定是在这两种遍历角度过程中产生的。

class Solution:
    def longestValidParentheses(self, s):
        left, right, idx, max_len_left = 0, 0, 0, 0
        tmp = 0
        while idx<=len(s)-1:
            if s[idx] == '(':
                left += 1
            else:
                right += 1                
                if right > left:
                    left, right, tmp = 0, 0, 0
                else:
                    tmp += 2
                    if left == right and tmp > max_len_left:
                        max_len_left = tmp
            idx += 1
        left, right, max_len_right, tmp  = 0, 0, 0, 0
        idx -= 1
        while idx >= 0:
            if s[idx] == ')':
                right += 1
            else:
                left += 1
                if left > right:
                    left, right, tmp = 0, 0, 0
                else:
                    tmp += 2
                    if left == right and tmp > max_len_right:
                        max_len_right = tmp
            idx -= 1
        return max(max_len_left, max_len_right)

