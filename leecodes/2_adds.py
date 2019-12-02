class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        pass

    def addTwoNumbers(self, l1, l2): # -> ListNode:
        n = l1.val + l2.val
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                    break
        return l3

if __name__ == '__main__':
    
    l1_list = [2, 4, 3] 
    l2_list = [9, 5, 6, 7]
    l1 = ListNode(0)
    l1_copy = l1
    for l1_index in l1_list:
        l1_copy.next = ListNode(l1_index)
        l1_copy = l1_copy.next
    l2 = ListNode(0)
    l2_copy = l2
    for l2_index in l2_list:
        l2_copy.next = ListNode(l2_index)
        l2_copy = l2_copy.next
    final_listnode = Solution().addTwoNumbers(l1.next, l2.next)
    print(final_listnode)
    p = final_listnode
    while True:
        if p:
            print(p.val)
            p = p.next
        else:
            break


