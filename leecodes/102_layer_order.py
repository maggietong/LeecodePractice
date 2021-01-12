class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def build_binary_tree(self, lst):
        node_lst = [None if v is None else Node(v) for v in lst]
        for index in range(1, len(node_lst)):
            node = node_lst[index]
            if node is not None:
                parent_index = (index - 1) // 2
                parent_node = node_lst[parent_index]
                if index % 2:
                    parent_node.left = node
                else:
                    parent_node.right = node
        return node_lst[0] if node_lst else None


if __name__=="__main__":
    t = BinaryTree()
    lst = [1, 2,3,None,4]
    print('lst=',lst)
    #import pdb; pdb.set_trace()
    t.root = t.build_binary_tree(lst)
    t.inorder(t.root)
    print(t.dump_nodes)