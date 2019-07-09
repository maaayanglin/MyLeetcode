# 执行用时 :72 ms, 在所有 Python3 提交中击败了94.81%的用户
# 内存消耗 :14.1 MB, 在所有 Python3 提交中击败了99.25%的用户
# 方法二：双指针法

  class Solution(object):
      def maxArea(self, height):
          max_area = 0
          l_index, r_index = 0, len(height)-1
          while l_index < r_index:
              if height[l_index] < height[r_index]:
                  area = (r_index-l_index)*height[l_index]
                  l_index += 1
              else:
                  area = (r_index - l_index) * height[r_index]
                  r_index -= 1
              if area > max_area:
                  max_area = area
          return max_area
