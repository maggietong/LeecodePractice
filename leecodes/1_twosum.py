class Solution(object):
    #def twoSum(self, nums, target):
    #    hashmap = {}
    #    for idx,num in enumerate(nums):
    #        hashmap[idx] = num
    #    for i,num in enumerate(nums):
    #        j = hashmap.get

    def twoSum(self, nums, target):
        lens = len(nums)
        j = - 1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j>0:
            return[j, i]

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 17]
    target = 22
    s = Solution()
    import pdb; pdb.set_trace()
    bias = s.twoSum(nums, target)
    print(bias)
