class Solution(object):
    def strStr(self, haystack, needle):
         # Func: calculate the bias
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st) + 1
            return dic

        if len(needle) > len(haystack):
            return -1
        if needle=="":
            return 0
        
        dic = calShiftMat(needle)
        idx = 0

        while idx+len(needle) <= len(haystack):
            str_cut = haystack[idx:idx+len(needle)]
            # judge if match
            if str_cut == needle:
                return idx
            else:
                # boundary handling
                if idx+len(needle) >= len(haystack):
                    return -1
                # don't match
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx+len(needle) >= len(haystack) else idx

if __name__ == "__main__":
    stra = "checkthisout"
    strb = "kth"
    s = Solution()
    import pdb; pdb.set_trace()
    bias = s.strStr(stra, strb)
    print(bias)
