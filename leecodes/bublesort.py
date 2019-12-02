
import os

class Solution(object):

    def sort(self, nums):
        hasChange = False
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    hasChange = True

if __name__ == "__main__":
    s = Solution()
    nums = [5,32, 12, 57, 5, 18, 3]
    s.sort(nums)
    for i in range(len(nums)):
        print("{0}".format(nums[i]));


