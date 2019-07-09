# 暴力法：简单地考虑每对可能出现的线段组合并找出这些情况之下的最大面积。

class Solution:
    def maxArea(self, height):
        d = {'area': 0}
        long = len(height)
        for l_index, val in enumerate(height):
            for r_index in range(l_index+1, long):
                area = (r_index - l_index) * min(val, height[r_index])
                if area > d['area']:
                    d['area'] = area
        return d['area']


if __name__ == '__main__':
    lt = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    o = Solution()
    a = time.time()
    res = o.maxArea(lt)
    b = time.time()
    print(res, 'time: ', b-a)
