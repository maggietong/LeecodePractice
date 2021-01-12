class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution(object):
    """
    a class for reversing the a single list
    """
    def __init__(self):
        pass
    
    def print_single_list(self, head):
        p = head
        while p != None:
            print(p.val)
            p = p.next

    def reverse_single_list(self, head=None):
        if head == None:
            return None
        if head.next == None:
            return head
        p1 = head
        tmp = None
        while p1 is not None:
            p2 = p1.next
            p1.next = tmp
            if p2 == None:
                ret = p1
                break
            new = p2.next
            p2.next = p1
            p1 = new
            if new == None:
                ret = p2
                break

            tmp = p2

        head.next = None
        return ret

if __name__ == "__main__":
    lst = 'ABCDEFG'
    p = Node(lst[0])
    head = p
    for i in range(1, len(lst)):
        p.next = Node(lst[i])
        p = p.next

    s = Solution()
    s.print_single_list(head)
    import pdb; pdb.set_trace()
    ret = s.reverse_single_list(head)
    head = ret
    s.print_single_list(head)

