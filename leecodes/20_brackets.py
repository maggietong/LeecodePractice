class Solution(object):
    def isValid(self, stra):
        dic = {
                '{':'}',
                '[':']',
                '(':')',
                '?':'?'
                }
        stack = ['?']
        for c in stra:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    s = Solution()
    stra = "{[[()]}"
    import pdb; pdb.set_trace()
    s.isValid(stra)

