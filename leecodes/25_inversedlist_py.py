class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None 

class NodeHandle(object):
    def __init__(self):
        self.head = None
    
    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def print(self):
        node = self.head
        while node:
            print('\n node: {0}, value: {1}, next: {2}'.format(node, node.val, node.next))
            node = node.next

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node

def print_list(head):
    node = head
    while node:
        print('\n node: {0}, value: {1}, next: {2}'.format(node, node.val, node.next))
        node = node.next



class Solution(object):
    def reverseKGroup(self, nodea, k):
        dummy = Node(0)
        dummy.next = nodea.head

        pre = dummy
        tail = dummy

        while True:
            count  = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre = head
            tail = head
        return dummy.next

if __name__=='__main__':
    nh = NodeHandle()
    
    for a in "abcdefghij": 
        nh.add(a)
        
    import pdb; pdb.set_trace()
    print_list(nh.head)
    s = Solution()
    import pdb; pdb.set_trace()
    head = s.reverseKGroup(nh, 3)
    print_list(head)
