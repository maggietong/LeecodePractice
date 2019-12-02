class Solution(object):
    def triple_sum(self, arr):
        arr.sort()
        length = len(arr)
        k = 0
        res = []
        for k in range(length-2):
            # arr[j] > arr[i] > arr[k]
            if arr[k] > 0:
                break
            if k > 0 and  arr[k] ==arr[k-1]:
                continue
            i, j = k+1, length-1
            while i < j:
                s = arr[k] + arr[i] + arr[j]
                if s < 0:
                    i += 1
                    while i < j and arr[i] == arr[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and arr[j] == arr[j+1]:
                        j -= 1
                else:
                    res.append([arr[k], arr[i], arr[j]])
                    i +=1
                    j -=1
                    while i < j and arr[i] == arr[i -1]:
                        i += 1
                    while i < j and arr[j] == arr[j+1]:
                        j -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    arr =  [5, 7, 3, -2, -6, 3, 19, -15, 2, 1, -1, -1,2,0]
    import pdb; pdb.set_trace()
    res = s.triple_sum(arr)
    print(res)
