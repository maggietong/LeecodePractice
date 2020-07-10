# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]

class BinaryTreeNode(object):
    def __init__(self, val='', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self):
        self.root = None
        self.dump_nodes=[]

    def create_binary_tree(self, root, lst, i):
        if i < len(lst):
            if lst[i] == None:
                return None
            root = BinaryTreeNode(lst[i])
            root.left = self.create_binary_tree(root, lst, i*2 + 1)
            root.right = self.create_binary_tree(root, lst, i*2 + 2)
            return root
        return None

    def build_binary_tree(self, lst):
        nodes = [None if v is None else BinaryTreeNode(v) for v in lst]
        for index in range(1,len(nodes)):
            node = nodes[index]
            if node is not None:
                parent_index = (index-1)//2
                parent_node = nodes[parent_index]
                if index % 2:
                    parent_node.left = node
                else:
                    parent_node.right = node
        return nodes[0] if nodes else None

    def add_node(self, data):
        if data == '#':
            node = '#'
        else:
            node = BinaryTreeNode(data)
        if self.root is None:
            self.root = node
            return
        tmp_queue = [self.root]
        while True:
            current_node = tmp_queue.pop(0)
            if current_node is None:
                return
            if current_node.left is None:
                current_node.left = node
                return
            elif current_node.right is None:
                current_node.right = node
                return
            tmp_queue.append(current_node.left)
            tmp_queue.append(current_node.right)

    def inorder(self, node):
        if node is None:
            return
        if node.left is not None:
            self.inorder(node.left)
        self.dump_nodes.append(node.val)
        if node.right is not None:
            self.inorder(node.right)

    def front_travel(self, node):
        if node == None:
            return
        if node.left != None:
            self.middle_travel(node.left)
        self.dump_nodes.append(node.val)
        if node.right != None:
            self.middle_travel(node.right)

    def front_travel(self, node):
        if node == None:
            return
        if node.left != None:
            self.middle_travel(node.left)
        if node.right != None:
            self.middle_travel(node.right)
        self.dump_nodes.append(node.val)

if __name__=="__main__":
    t = BTree()
    lst = [1, 2,3,None,4]
    print('lst=',lst)
    #import pdb; pdb.set_trace()
    t.root = t.build_binary_tree(lst)
    t.inorder(t.root)
    print(t.dump_nodes)


