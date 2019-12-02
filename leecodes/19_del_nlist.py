class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def remove_nth_from_end(self, head, n):
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        slow = dummy
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    l1_list = [9,5,3,5,7,8]
    l1 = ListNode(0)
    head = l1
    for l1_index in l1_list:
       l1.next =ListNode(l1_index)
       l1 = l1.next
    s = Solution()
    import pdb; pdb.set_trace()
    out = s.remove_nth_from_end(head, 2)
    print(out)

