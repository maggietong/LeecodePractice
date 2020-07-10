"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""
class BinaryTreeNode(object):
    def __init__(self, data=0, lchild=None, rchild=None):
        self.val = data
        self.left = lchild
        self.right = rchild
# create a binary tree with input_list
def create_binary_tree(lst):
    nodes = [None if v is None else BinaryTreeNode(v) for v in lst]
    for index in range(1, len(nodes)):
        node = nodes[index]
        if node is not None:
            parent_index = (index - 1)//2
            parent_node = nodes[parent_index]
            setattr(parent_node, 'left' if index % 2 else 'right', node)
    return nodes[0] if nodes[0] else None

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        pass

    def is_valid_BST(self, root):
        root_val = root.val
        nodes = []
        def verify_2btree(node):
            if node == None:
                return True
            if node.left == None and node.right == None:
                nodes.append(node.val)
                return True
            cur = node.val
            # left node
            node_left = node.left
            if node_left is not None:
                b = verify_2btree(node_left)
                if b is False:
                    return False
                if node_left.val >= cur:
                    return False
            nodes.append(cur)
            # right node
            node_right = node.right
            if node_right is not None:
                b = verify_2btree(node_right)
                if b is False:
                    return False
                if node_right.val <= cur:
                    return False
            return True
        ret = verify_2btree(root)
        if ret is False:
            return False
        print('The nodes vals=', nodes)
        for i in range(len(nodes)-1):
            if nodes[i+1] <= nodes[i]:
                return False
        return True
    def is_valid_BST_preorder(self, root):
        nodes = []
        def preorder(node):
            if node is None:
                return
            if node.left==None and node.right==None:
                nodes.append(node.val)
                return
            if node is not None:
                if node.left is not None:
                    preorder(node.left)
                nodes.append(node.val)
                if node.right is not None:
                    preorder(node.right)
            return
        preorder(root)
        print("The nodes vals=", nodes)

        for i in range(len(nodes) - 1):
            if nodes[i + 1] <= nodes[i]:
                return False
        return True


if __name__ == "__main__":
    stra = ['5','1','4', '3', '6']
    #root = Node('A', Node('B', Node('D')), Node('C', Node('E'), Node('F')))
    #root_a = Node('5', Node('1', Node('4')), Node('3', Node('6'), Node('7')))
    #root_a = Node('2', Node('1'), Node('3'))
    #root_a = Node('10', Node('5'), Node('15', Node(None,Node(None)), Node('6', None, Node('20'))))
    #root_a = Node('5', None, Node('0'))
    #input_data = ['3', '2', '6', None, '4', '5', '7']
    input_data = [3, 1,5,0,2,4,6,None,None,None,3]
    root = create_binary_tree(input_data)
    s = Solution()
    print('The result=', s.is_valid_BST(root))
    print('The result=', s.is_valid_BST_preorder(root))

