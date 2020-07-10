"""
KMP 算法实现
首先求出pattern字符串的next（j）函数，next函数指的是当pattern字符中第几个字符失配时，
在模式中需要重新和主串中该字符进行比较的字符的第一个位置，
求得next函数之后，对主串做窗口滑动就可以得到要的结果
"""
class Solution(object):
    def __init__(self):
        pass

    def next_func(self, p, j):
        if j==1:
            next = 0
            return next

    def match_patt(self, strs):
        patt = "abaabcac"
        next = {
                1:0,
                2:1,
                3:1,
                4:2,
                5:2,
                6:3,
                7:1,
                8:2
                }
        if strs == '' or len(strs) < len(patt):
            return None

        i = 0
        j = 0
        while i < len(strs) and j < len(patt):
            if strs[i] == patt[j]:
                if j == len(patt) - 1:
                    print(i,j)
                    return i-j
                i = i+1
                j = j+1
            else:
                nv = next[j+1]
                if nv == 0:
                    i = i+1
                    j = 0
                else:
                    j = nv - 1
        return None



if __name__ == "__main__":
    s = Solution()
    strs = "ababceabdabaabcacd"

    import pdb; pdb.set_trace()
    print(s.match_patt(strs))

