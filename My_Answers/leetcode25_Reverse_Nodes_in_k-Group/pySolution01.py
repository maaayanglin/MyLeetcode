

# 思路：
# 新建一个哨兵头结点guard用于简化代码编写
#        guard = ListNode(0)
#        guard.next = head
# 先顺序遍历链表，记录满足k个节点的总组数total，第total+1组节点将保持原有顺序
#        tmp = head
#        count = 0
#        nums_of_group = 0
#        while tmp:
#            count += 1
#            if count % k == 0:
#                nums_of_group += 1
#            tmp = tmp.next    
# 外循环nums_of_group次，每次循环一开始，我们需要知道当前组的前驱节点pre_of_group，第一次循环其为guard
#        pre_of_group = guard
#        for _ in range(nums_of_group):
# 由pre_of_group确定：
#            pre = pre_of_group.next
#            cur = pre.next
#            nex = cur.next
# 再进行组内链表翻转(循环k-1次)，在最后一次翻转时需要另外保存组的后继节点next_of_group(其实就是nex指向的位置)
#            cur.next = pre
#            pre, cur, nex = cur, nex, nex.next
# 组内链表翻转后还要对该组的头尾与组的前驱、后继节点分别重新对接，完成组内翻转后组内新的末端节点为原pre_of_group.next，新头节点为cur
#            pre_of_group.next.next = nex  # 将组内新末端节点对接后组的后继节点
#            cur.next = pre_of_group # 将组内新的头节点对接到组的前驱节点
# 对接完成后初始化下一组的前驱节点，其位置就是当前组的新末端节点pre_of_group.next
#            pre_of_group = pre_of_group.next
# 循环结束，返回结果
#        return guard.next


