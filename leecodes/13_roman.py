class Solution:
    def romanToInt(self, s):
        dic = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
        ans = 0
        for i, char in enumerate(s[:-1]):
            if dic[char] >= dic[s[i+1]]:
                ans += dic[char]
            else:
                ans -= dic[char]

        ans += dic[s[-1]]
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "MCMXCIV"
    import pdb; pdb.set_trace()
    ret = sol.romanToInt(s)
    print(ret)
