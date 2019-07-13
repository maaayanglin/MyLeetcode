# 执行用时 :48 ms, 在所有 Python3 提交中击败了89.36%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了83.01%的用户

# 方法：采用双指针法，走在前面的指针q.next为空时表示到达末尾，此时pre位置为需要删除节点的前驱节点。另外在head前添加哨兵位guard用于简化代码。

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        guard = ListNode(0)
        guard.next = head
        pre = q = guard       
        for _ in range(n):
            q = q.next
        while q.next:
            pre = pre.next
            q = q.next
        pre.next = pre.next.next
        return guard.next
