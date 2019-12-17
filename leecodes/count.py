class Solution(object):
    def count(self, arr):
        """
        arr: imput array
        """
        n = len(arr)
        cdict = {}
        for i in range(n):
            if arr[i] in cdict.keys():
                cdict[arr[i]] += 1
            else:
                #cdict[arr[i]] = 1
                cdict.update({arr[i]:1})

        return cdict

    def counta(self, arr):
        n = len(arr)
        cdict = {}
        for i in range(n):
            flag = 0
            for j in cdict.keys():
                if arr[i] == j:
                    cdict[j] += 1
                    flag = 1
                    break;
            if flag == 0:
                cdict.update({arr[i]:1})
        return cdict


if __name__=="__main__":
    sol = Solution()
    arr = ['a', 'a','b', 'a', 'b', 'c']
    output = sol.counta(arr)
    print(output)
