# my answer01：
# 执行用时 :120 ms, 在所有 Python3 提交中击败了42.67%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了94.77%的用户
# 方法：按行访问


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or not s:
            return s
        tmp = s
        l = []
        count = 2*numRows - 2  # 4 + 2 * (numRows - 3) 
        while True:  # 将每一个"Z"单独切割出来，每个‘Z’含有count个元素（除最后一个‘Z’可能元素不满外）
            l.append(tmp[0:count])
            tmp = tmp[count:]
            if not tmp:
                break
        l_match = ['' for i in range(count)]
        for i in range(len(l[0])):  # 将切割出来的每一个“Z”按其索引的位置拼接起来
            for j in l:
                try:
                    l_match[i] += j[i]
                except:
                    pass
        ret = l_match[0]
        for sa, sb in zip(l_match[1:numRows-1], reversed(l_match[numRows:])):
            l_outer = list(sa)
            loca = 0
            for ele in sb:
                l_outer.insert(loca*2+1, ele)
                loca += 1
            ret += ''.join(l_outer)
        ret += l_match[numRows-1]
        return ret


if __name__ == '__main__':
    st = 'leetcodeishiring'
    obj = Solution()
    res = obj.convert(st, 4)
    print(res)
