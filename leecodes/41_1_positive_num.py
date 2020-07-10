"""
41. 缺失的第一个正数
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2
示例 3:
输入: [7,8,9,11,12]
输出: 1
提示：
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
class Solution(object):
    def __init__(self):
        pass
    def minimum_num(self, nums):
        length = len(nums)
        for i in range(1, length+1):
            if i not in nums:
                return i
        return length+1

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5]
    nums = [3,4,5,6,7]
    nums = [3,4,-1,1]
    print(s.minimum_num(nums))

