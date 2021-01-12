class Solution(object):
    def __init__(self):
        pass

    def __str__(self):
        print("quick sort a list")

    def sort(self, lst):
        if lst == None:
            return None
        if len(lst)  == 1:
            return lst

        def back_trace(begin, end):
            if begin > end:
                return
            # one member
            if end == begin:
                return
            # two member
            if end-begin == 1:
                if lst[begin] > lst[end]:
                    lst[begin], lst[end] = lst[end], lst[begin]
                return
            # size > 2
            i = begin
            j = end
            k = begin
            while i < j:
                while (lst[j] > lst[k]) and (i<j):
                    j -= 1
                while (lst[i] < lst[k]) and (i<j):
                    i += 1
                if j > i:
                    lst[i], lst[j] = lst[j], lst[i]
            if lst[k] > lst[i]:
                lst[i],lst[k] = lst[k], lst[i]
            print('-----1')
            print(lst)
            #        import pdb; pdb.set_trace()
            back_trace(begin, i-1)
            print('------2')
            print(lst)
            back_trace(i+1, end)
            print('------3')
            print(lst)

        begin = 0
        end = len(lst) - 1
        back_trace(begin, end)

if __name__ == "__main__":
    import random
    lst = [8,9,1,3,5,7,2,4,6]
    import pdb;
    pdb.set_trace()
#    random.shuffle(lst)
    print(lst)
    s = Solution()

    s.sort(lst)


