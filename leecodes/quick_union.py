"""
Quick to return True or False whether the two objects is connected or not, UF
"""
class Node(object):
    def __init__(self, val=''):
        self.val = val

class UnionFind(object):
    def __init__(self):
        '''
        create a UnionFind based on inputs
        '''
        print("Please type in the node of object:")
        inw = ''
        self.node_arr = []
        self.node_arr = [Node(i) for i in range(10)]
        # while inw != 'End':
        #     inw = input()
        #     try:
        #         w = int(inw)
        #         nd = Node(w)
        #         nd.root = nd
        #         self.node_arr.append(nd)
        #     except Exception as e:
        #         print("The input is incorrect, please try again or type in 'End' to stop input new data")
        #         pass
        self.id_arr = [ id for id in range(len(self.node_arr))]

    def union(self, p, q):
        tmp = self.id_arr[q]
        for idx,val in enumerate(self.id_arr):
            if val == tmp:
                self.id_arr[idx] = self.id_arr[p]
        print(p,q, '    ', self.id_arr)

    def is_connected(self, a, b):
        if self.id_arr[a] == self.id_arr[b]:
            return True
        return False

    def _root(self, q):
        while  self.id_arr[q]!= q:
            q = self.id_arr[q]
        return q

    def union_quick(self, p, q):
        q = self._root(q)
        self.id_arr[q]= self.id_arr[p]
        print(p,q,'    ',self.id_arr)

    def is_connected_quick(self, a, b):
        if self._root(a) == self._root(b):
            return True
        return False

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    uf = UnionFind()
    p = 3
    q = 8
    # uf.union(p, q)
    # uf.union(6,9)
    # uf.union(3, 6)
    # uf.union(4,9)
    # print(uf.is_connected(8,9))
    # print(uf.is_connected(3, 5))
    # print(uf.is_connected(4,3))
    # print(uf.is_connected(1, 3))
    uf.union_quick(3, 4)
    uf.union_quick(4,5)
    uf.union_quick(6, 7)
    uf.union_quick(8,6)
    uf.union_quick(4, 6)
    uf.union_quick(2, 1)
    uf.union_quick(3, 2)
    print(uf.is_connected_quick(8,9))
    print(uf.is_connected_quick(3, 5))
    print(uf.is_connected_quick(7,3))
    print(uf.is_connected_quick(8, 0))