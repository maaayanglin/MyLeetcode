# 执行用时 :36 ms, 在所有 Python3 提交中击败了99.48%的用户
# 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了32.91%的用户

# 思路：用三个指针分别指向相邻节点对的第一个节点cur、cur的前驱节点pre、相邻节点对之后的第一个节点behind。每轮完交换移动指针即可。
#       终止条件为cur为空（偶数个节点）或者cur.next（奇数个节点）为空。
#       指针示意： pre -> cur -> cur.next -> behind -> ...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# guard -> 2 -> 1 -> 3 -> 4
class Solution:
    def swapPairs(self, head):
        if not head or head.next==None:
            return head
        guard = pre = ListNode(0)       
        guard.next = head
        cur = pre.next
        behind = cur.next.next
        while True:
            pre.next = cur.next
            cur.next.next = cur
            cur.next = behind
            
            pre = cur
            cur = cur.next
            if not cur or not cur.next:
                break
            behind = cur.next.next
        return guard.next

