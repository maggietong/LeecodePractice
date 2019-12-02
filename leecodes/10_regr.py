class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or \
                    first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

def fib(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        a, b = b, a+b

def fibonacci(i):
    num_list = [0, 1]
    if i < 2:
        return num_list[i]
    elif i >= 2:
        return (fibonacci(i-2) + fibonacci(i-1))

if __name__ == "__main__":
    text = 'aa'
    pattern = 'a*'
    import pdb; pdb.set_trace()
    fib(10000)
    fibonacci(1000)
    s = Solution()
    a = s.isMatch(text, pattern)
    print a
