# 执行用时 :80 ms, 在所有 Python3 提交中击败了46.40%的用户
# 内存消耗 :14.5 MB, 在所有 Python3 提交中击败了5.00%的用户

# 思路：双指针法：
# 维护左右指针left、right。若把跨度最大的可盛水结构看作是一个容器，left指向容器最左柱子，right指向容器的最右柱子。
# 若把容器内盛水的部分看做是一个个小碗，整体思路是从边缘的碗开始取水，确定碗的范围后取水，通过移动指针，去除该碗后构建新的容器。循环直至容器内无碗。
# 指针移动的规则(即确定碗的范围)：
#   指针指向的柱子短的一端往高的一端移动，直到遇到柱子高于或等于容器短端高度，这样才能保证取的碗是完整的碗，而不是碗中的小碗。
# 构建新容器则只需将取完碗后的指针继续移动直至无无效柱子。无效柱子是指容器边缘无法盛水的部分。

class Solution(object):
    def __init__(self):
        self.water = 0
        self.finish = False

    def trap(self, height):
        while True:
            height = self.clear_both(height)
            if not height:
                break
            dire = True if height[0] <= height[-1] else False
            height = self.cut_down(height, dire)
        return self.water

    # 计算给定范围的盛水量
    def calculate_water(self, ls, surface_of_water):
        self.water += len(ls) * surface_of_water - sum(ls)
        return self.water

    # 确定碗的范围。从容器两端较短的一端往较长的一端移动，并将移动端所能盛的水计算出来。dire=True为左指针往右移动
    def cut_down(self, height, dire=True):
        if dire is not True:
            height = height[::-1]
        idx = 1
        while True:
            if height[idx] >= height[0]:
                break
            idx += 1
        self.calculate_water(height[1:idx], min(height[0], height[idx]))
        return height[idx:] if dire else height[idx:][::-1]

    # 构建新容器，去除两端无用柱子
    def clear_both(self, height):
        left, right = 0, 0
        while True:
            if left >= len(height)-1 or height[left] > height[left+1]:
                break
            left += 1
        r_height = height[::-1]
        while True:
            if right >= len(r_height)-1 or r_height[right] > r_height[right+1]:
                break
            right += 1
        right = len(r_height) - 1 - right
        if left >= right:
            self.finish = True
            return []
        return height[left:right+1]
