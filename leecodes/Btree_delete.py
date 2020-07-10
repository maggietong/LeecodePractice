"""
Huffman tree and huffman encoding and decodeing
create_huffman()
encode()
decode()
"""
class Node(object):
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def compare(self, nod):
        if self.item <= nod.item:
            return True
        else:
            return False

class HuffmanTree(object):
    def __init__(self):
        self.root = None

    def create_huffman(self, arr_r):
        if len(arr_r) == 0:
            return None
        if len(arr_r) < 2:
            root = Node(item=arr_r[0])
            return root
        probility = []
        for i in range(len(arr_r)):
            nod = Node(arr_r[i])
            arr.append(nod)

        head = Node(item=arr[0])
        while len(arr) >= 2:
            arr = sorted(arr, key=lambda nod:nod.item)
            left = arr.pop(0)
            right = arr.pop(0)
            father_val = left.item + right.item
            father = Node(item=father_val)
            arr.append(father)
            arr = sorted(arr, key=lambda nod:nod.item)
            father.left = left
            father.right = right
        self.root = father

    def preorder(self, root):
        cur = root
        print(cur.item)
        if cur.left != None:
            self.preorder(cur.left)
        if cur.right != None:
            self.preorder(cur.right)


if __name__ == "__main__":
    arr = [13,7,8,3,29,6,1]
    arr = "My name is maggie. I am a software engineer"
    tree = HuffmanTree()
    import pdb; pdb.set_trace()
    head = tree.create_huffman(arr)
    tree.preorder(tree.root)


