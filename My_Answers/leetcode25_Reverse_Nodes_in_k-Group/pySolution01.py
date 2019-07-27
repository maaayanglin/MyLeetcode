# 执行用时 :64 ms, 在所有 Python3 提交中击败了94.44%的用户
# 内存消耗 :14.5 MB, 在所有 Python3 提交中击败了11.77%的用户

# 思路：
# 先排除head为空或k为1的特殊情况：
#        if not head or k == 1:
#            return head
# 新建一个哨兵头结点guard用于简化代码编写
#        guard = ListNode(0)
#        guard.next = head
# 先顺序遍历链表，记录满足k个节点的总组数total_groups，第total_groups+1组节点将保持原有顺序
#        tmp = head
#        count = 0
#        total_groups = 0
#        while tmp:
#            count += 1
#            if count % k == 0:
#                total_groups += 1
#            tmp = tmp.next    
# 外循环total_groups次，每次循环一开始，我们需要知道当前组的前驱节点pre_of_group，第一次循环其为guard
#        pre_of_group = guard
#        for _ in range(total_groups):
# 由pre_of_group确定：
#            pre = pre_of_group.next
#            cur = pre.next
#            nex = cur.next
# 再进行组内链表翻转(循环k-1次)，在最后一次翻转时需要另外保存组的后继节点next_of_group(其实就是nex指向的位置)
#            for i in range(k-1):
#                cur.next = pre
#                if i < k-2:  # 因为cur的初始化位置是组内第二个元素位置，即使得辅助指针移动次数比交换方向次数少1
#                    pre, cur, nex = cur, nex, nex.next
# 组内链表翻转后还要对该组的头尾与组的前驱、后继节点分别重新对接，完成组内翻转后组内新的末端节点为原pre_of_group.next，新头节点为cur
#            pre_of_group.next.next = nex  # 将组内新末端节点pre_of_group.next对接后组的后继节点nex
#            new_end_of_group = pre_of_group.next  # 要保留住组内新的末端节点
#            pre_of_group.next = cur # 将组的前驱节点pre_of_group对接到组内新的头节点cur
# 对接完成后初始化下一组的前驱节点，其位置就是当前组的新末端节点pre_of_group.next
#            pre_of_group = new_end_of_group
# 循环结束，返回结果
#        return guard.next

# 完整代码如下：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        guard = ListNode(0)
        guard.next = head
        
        tmp = head
        count = 0
        total_groups = 0
        while tmp:
            count += 1
            if count % k == 0:
                total_groups += 1
            tmp = tmp.next
        pre_of_group = guard
        for _ in range(total_groups):
            pre = pre_of_group.next
            cur = pre.next
            nex = cur.next
            
            for i in range(k-1):
                cur.next = pre
                if i != k-2:
                    pre, cur, nex = cur, nex, nex.next
                
            pre_of_group.next.next = nex
            new_end_of_group = pre_of_group.next
            pre_of_group.next = cur
            pre_of_group = new_end_of_group
        return guard.next
