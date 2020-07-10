class BinaryTreeNode(object):
    def __init__(self, data=0, lchild=None, rchild=None):
        self.data = data
        self.left = lchild
        self.right = rchild
# create a binary tree with input_list
def create_binary_tree(root, input_data, i):
    if i < len(lst):
        if lst[i] == '#':
            return None
        else:
            root = BinaryTreeNode(lst[i])
            root.left = create_binary_tree(root.left, lst, 2*i + 1)
            root.right = create_binary_tree(root.right, lst, 2*i + 2)
            return root
    return root

if __name__ == "__main__":
    input_data = ['1','2','3','#','4','5','6', '7', '8', '9']
    root = create_binary_tree(None, input_data, 0)