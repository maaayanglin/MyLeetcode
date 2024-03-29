# Palindrome_Number
leetcode题目009: 回文数

方法：反转一半数字
思路

映入脑海的第一个想法是将数字转换为字符串，并检查字符串是否为回文。但是，这需要额外的非常量空间来创建问题描述中所不允许的字符串。

第二个想法是将数字本身反转，然后将反转后的数字与原始数字进行比较，如果它们是相同的，那么这个数字就是回文。 但是，如果反转后的数字大于 \text{int.MAX}int.MAX，我们将遇到整数溢出问题。

按照第二个想法，为了避免数字反转可能导致的溢出问题，为什么不考虑只反转 \text{int}int 数字的一半？毕竟，如果该数字是回文，其后半部分反转后应该与原始数字的前半部分相同。

时间复杂度：O(log 10​	(n))，对于每次迭代，我们会将输入除以10，因此时间复杂度为O(log 10​	(n))。
空间复杂度：O(1)。

链接：https://leetcode-cn.com/problems/two-sum/solution/hui-wen-shu-by-leetcode/
来源：力扣（LeetCode）
