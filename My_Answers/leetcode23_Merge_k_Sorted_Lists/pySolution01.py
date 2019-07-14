# 执行用时 :100 ms, 在所有 Python3 提交中击败了82.33%的用户
# 内存消耗 :16.6 MB, 在所有 Python3 提交中击败了52.16%的用户

# 思路：将每一链表按头结点value值的倒序排好并将排序后的各链表头结点保存在一个列表sort_queue中，即利用了优先队列的思路，
# 每循环一次弹出列表末尾的头结点即是value值最小的节点min_node，
# 用follow指针指向取出的的最小value的节点，min_node指针后移，将min_node指向的当前节点继续按其value值大小有序地插入sort_queue中，
# 使sort_queue的末尾元素始终是最小value的节点，follow后移。继续取上述操作直到sort_queue为空
# 空间复杂度：因为要维护一个存放k条链表的当前节点的列表，故需要 O(k) 的空间复杂度
# 时间复杂度：在长度为k的列表中插入一个节点时间复杂度为k，遍历所有节点时间复杂度为N=n*k，
#            其中k为需要合并的链表数，n为每条链表的平均长度，N=k*n表示总结点数,因此时间复杂度为 O(k*N)
# 进一步优化：在比较插入时可以采用时间复杂度为logn的二分法。也可以利用python模块Queue的优先队列PriorityQueue。优化后时间复杂度为O(Nlogk)

class Solution:
    def mergeKLists(self, lists):
        guard = follow = ListNode(0)
        lists = filter(None, lists)
        sort_queue = list(sorted(lists, key=lambda node: node.val, reverse=True))
        while sort_queue:
            min_node = sort_queue.pop()
            follow.next = min_node
            min_node = min_node.next
            if min_node:
                tag = True
                len_of_queue = len(sort_queue)
                for idx, node in enumerate(sort_queue[::-1]):
                    if node.val > min_node.val:
                        tag = False
                        sort_queue.insert(len_of_queue-idx, min_node)
                        break
                if tag:
                    sort_queue.insert(0, min_node)
            follow = follow.next
        return guard.next
