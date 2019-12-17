class Solution(object):
    def mat_mux(self, a, b, m, n, l):
        matrixc=[[]]
        matrixc = [[0 for i in range(l)] for i in range(m)]
        for i in range(m):
            for j in range(l):
                for z in range(n):
                    matrixc[i][j] += a[i][z]*b[z][j]
        return matrixc

if __name__=="__main__":
    s = Solution()
    matrixa=[[]]
    matrixb=[[]]
    m = 3
    n = 4
    l = 5
    import pdb; pdb.set_trace()
    matrixa = [[0 for i in range(n)] for i in range(m)]
    matrixb = [[0 for i in range(l)] for i in range(n)]
    for i in range(3):
        for j in range(4):
            a = input("input one digit:")
            matrixa[i][j] = int(a)

    import pdb; pdb.set_trace()
    for i in range(4):
        for j in range(5):
            a = input("input one digit:")
            matrixb[i][j] = int(a)
    import pdb; pdb.set_trace()
    print(matrixa)
    print("----")
    print(matrixb)
    val = s.mat_mux(matrixa, matrixb, m, n, l)
    print(val)


       
