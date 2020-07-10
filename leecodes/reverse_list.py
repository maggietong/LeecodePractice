class Node(object):
    def __init__(self, val='', next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        pass

    def reverse_lst(self, head):
        if head == None:
            return None
        p1 = head
        head.next = None
        while p1 is not None:
            p2 = p1.next
            p3 = p2.next
            tmp = p3.next
            # reverse
            p2.next = p1
            p3.next = p2
            p1 = tmp
        head = p1
        return head

    def reverse_lst_node(self, head):
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
            if p1 == None:
                ret = p2
                break
            tmp = p2

        head.next = None
        return ret

if __name__ == "__main__":
    lst = 'ABCDEFG'
    tmp = Node(lst[0])
    head = tmp
    for a in lst[1:]:
        tmp.next = Node(a)
        tmp = tmp.next
    p = head
    while p != None:
        print(p.val)
        p = p.next
    print('------')
    s = Solution()
    import pdb; pdb.set_trace()
    ret = s.reverse_lst_node(head)
    while ret != None:
        print(ret.val)
        ret = ret.next



