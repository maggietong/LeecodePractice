class Solution(object):
    def removeDup(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    nums = [2, 5, 5,5, 7,8,8]
    s = Solution()
    import pdb; pdb.set_trace()
    s.removeDup(nums)
