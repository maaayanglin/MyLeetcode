# ZigZag_Conversion #
## leetcodes题目006：Z字形变化 ##

方法一：按行排序 思路

通过从左向右迭代字符串，我们可以轻松地确定字符位于 Z 字形图案中的哪一行。

算法

我们可以使用 min(numRows,len(s)) 个列表来表示 Z 字形图案中的非空行。

从左到右迭代 s，将每个字符添加到合适的行。可以使用当前行和当前方向这两个变量对合适的行进行跟踪。

只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。

复杂度分析

时间复杂度：O(n)，其中 n == len(s) 空间复杂度：O(n)

方法二：按行访问 思路

按照与逐行读取 Z 字形图案相同的顺序访问字符串。

算法

首先访问 行 0 中的所有字符，接着访问 行 1，然后 行 2，依此类推...

对于所有整数 k，

行 0 中的字符位于索引 k(2⋅numRows−2) 处; 行 numRows−1 中的字符位于索引 k(2⋅numRows−2)+numRows−1 处; 内部的 行 i 中的字符位于索引 k(2⋅numRows−2)+i 以及 (k+1)(2⋅numRows−2)−i 处;

链接：https://leetcode-cn.com/problems/two-sum/solution/z-zi-xing-bian-huan-by-leetcode/ 来源：力扣（LeetCode）
