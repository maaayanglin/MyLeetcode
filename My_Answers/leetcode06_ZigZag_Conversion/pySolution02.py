#  解题方法2
#  执行用时 :68 ms, 在所有 Python3 提交中击败了99.37%的用户
#  内存消耗 :13.1 MB, 在所有 Python3 提交中击败了94.94%的用户

#  方法：按行排序
#  思路：通过从左向右迭代字符串，我们可以轻松地确定字符位于 Z 字形图案中的哪一行。
#  实现逻辑：当前字符行号为index，下一个字符的行号为 index + vector ，其中vector值为±1 ，当index等于第一行或最后一行时，改变vector的方向。


class Solution(object):
    def convert(self, s, numRows):
        if not s or numRows == 1:
            return s
        ls = [''] * numRows
        index = 0
        vector = 1
        for ele in s:
            ls[index] += ele
            index += vector
            if index in (0, numRows-1):  #  当index等于第一行或最后一行时，改变vector的方向
                vector = -vector
        ret = ''.join(ls)
        return ret


if __name__ == '__main__':
    st = 'leetcodeishiring'
    obj = Solution()
    res = obj.convert(st, 4)
    print(res)
