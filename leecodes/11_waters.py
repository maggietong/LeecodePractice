class Solution(object):
    def max_area(self, height):
        i = 0
        j = len(height)-1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    max_value = s.max_area(height)
    print(max_value)

