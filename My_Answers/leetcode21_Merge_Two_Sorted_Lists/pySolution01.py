# 执行用时 :52 ms, 在所有 Python3 提交中击败了92.78%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了58.54%的用户

# 逐次比较l1、l2的值，较小的插入follow的末尾，指针后移。其中一方为空时follow的末尾直接指向另一方。时间复杂度：O(min(len(l1), len(l2))),空间复杂度O(1)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = follow = ListNode(0)
        while True:
            if not l1:
                follow.next = l2
                break
            if not l2:
                follow.next = l1
                break
            if l1.val <= l2.val:
                follow.next = l1
                l1 = l1.next
            else:
                follow.next = l2
                l2 = l2.next
            follow = follow.next
        return guard.next
