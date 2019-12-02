class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                res = res + c[0]
            else:
                break
        return res

if __name__ == "__main__":
    s = Solution()
    strs = []
    #strs = ["flowers", "flow", "flight"]
    import pdb; pdb.set_trace()
    s.longestCommonPrefix(strs)

