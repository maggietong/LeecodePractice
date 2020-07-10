# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution(object):
    def __init__(self, lst):
        self.lst = lst
        self.output = []
        pass

    def list_all(self):
        def back_track(combination, depth):
            if depth == 0:
                self.output.append(combination)
            else:
                depth -= 1
                for ch in list(set(self.lst)-set(combination)):
                    print('Before back', depth)
                    print(combination, ch)
                    back_track(combination+ch, depth)
                    print('after back', depth)

        lst_depth = len(self.lst)
        back_track('', lst_depth)


if __name__ == "__main__":
    lst = ['1', '2', '3']
    import pdb; pdb.set_trace()
    s = Solution(lst)
    s.list_all()
    print(s.output)

