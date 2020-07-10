"""
give n lists, please print the top K maximum values in these n lists
using bubble sort to get the top k values in each list, then compose a new list, then using bubble sort to print the top k max value for the new list
"""
class TopK(object):
    def __init__(self):
        pass

    def __str__(self):
        print("top k values in n lists")

    def list_top_k(self, lsta, k):
        k_dict = {}
        for lst in lsta:
            self.bubble_sort(lst, k)
            print(lst)
        lstb = []
        for lst in lsta:
            lst = lst[::-1]
            lstb.extend(lst[0:k])
        self.bubble_sort(lstb, k)
        lstb = lstb[::-1]
        print(lstb[0:k])
        return lstb[0:k]

    def bubble_sort(self, nums, k):
        '''
        bubble sort the K maximum values for list nums
        '''
        hasChange = False
        n = len(nums)
        for i in range(k):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    hasChange = True


if __name__=="__main__":
    t = TopK()
    # ID, city, counts
    lsta = [[ 20, 30, 13, 5, 156, 67, 357, 2, 999],
             [ 30, 50, 32, 24, 3, 5, 7],
             [ 178, 234, 123, 7, 9, 10],
             [ 1345, 236, 500, 3],
             [ 2, 9, 7, 35, 678, 157892],]

    import pdb; pdb.set_trace()

    ret = t.list_top_k(lsta, k=3)
    print("The top k values are:")
    print(ret)