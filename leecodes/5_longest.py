class Solution(object):
    def longest(self, stra):
        size = len(stra)
        if size <= 1:
            return s
        #dp problem
        #dp[l,r]:stra[l,r]
        dp = [[False for _ in range(size)] for _ in range(size)]
        longest_l = 1
        res = stra[0]
        
        for r in range(1, size):
            for l in range(r):
                if stra[l]==stra[r] and (r-l <=2 or dp[l+1][r-1]):
                    dp[l][r]=True
                    cur_len = r-l+1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = stra[l:r+1]

            # debug
            for item in dp:
                print(item)
            print('---')
        return res
        
if __name__ == "__main__":
    stra = "babad"
    strb = "kth"
    s = Solution()
    import pdb; pdb.set_trace()
    bias = s.longest(stra)
    print(bias)
