

# 思路：
# 先顺序遍历链表，记录满足k个节点的总组数total，第total+1组节点将保持原有顺序
# 外循环total次，
# 每次循环一开始，我们需要知道当前组的前驱节点pre_of_group
# 由pre_of_group确定：
#     1、pre = pre_of_group.next
#     2、cur = pre.next
#     3、nex = cur.next
# 再进行组内链表翻转(循环k-1次)，在最后一次翻转时需要另外保存组的后继节点next_of_group(其实就是nex指向的位置)
#     1、cur.next = pre
#     2、pre, cur, nex = cur, nex, nex.next
# 组内链表翻转后还要对该组的头尾与组的前驱、后继节点分别重新对接，完成组内翻转后组内新的末节点为原pre_of_group.next，新头节点为cur
#     1、pre_of_group.next.next = nex  # 将组内新末节点对接后组的后继节点
#     2、cur.next = pre_of_group # 将组内新的头节点对接到组的前驱节点
# 对接完成后初始化下一组的前驱节点：
#     1、pre_of_group = 


