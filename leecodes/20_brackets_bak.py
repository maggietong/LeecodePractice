class Solution(object):
    def isValid(self, stra):
        dic = {
                ')':'(',
                ']':'[',
                '}':'{',
                }
        stack = []
        for c in stra:
            if c in dic:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if dic[c] != top_element:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    s = Solution()
    stra = "{[[(2*2)]]}"
    import pdb; pdb.set_trace()
    print(s.isValid(stra))

