class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2
        return prehead.next

if __name__=="__main__":
    l1_list = [1,2,4]
    l2_list = [1, 3, 4]
    l1 = ListNode(0)
    l2 = ListNode(0)
    l1_head = l1
    l2_head = l2
    for l1_index in l1_list:
        l1.next = ListNode(l1_index)
        l1 = l1.next
    for l2_index in l2_list:
        l2.next = ListNode(l2_index)
        l2 = l2.next

    s = Solution()
    import pdb; pdb.set_trace()
    out = s.mergeTwoLists(l1_head,l2_head)
    while out:
        print(out.val)
        out = out.next
