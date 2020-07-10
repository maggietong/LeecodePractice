# 91.一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

class Solution(object):
    def __init__(self):
        pass

    def __str__(self):
        print("number decoding")
    def num_decoding(self, lst):
        """
        :type s: str
        :rtype: int
        """
        def back_trace(chr, sub_str):
            ret_str = []
            if len(sub_str) == 0:
                ret_str.append(chr)
                return ret_str
            for sub in sub_str:
                # special case
                if chr == '0':
                    if sub[0] == '0':
                        return 0
                    else:
                        ret_str.append(chr + ',' + sub)
                    continue
                # after chr != 0
                # sub[0] == 0
                # a,b branch
                if sub[0] == '0':
                    if chr > '2':
                        return 0
                else:
                    sub_a = chr + ',' + sub
                    ret_str.append(sub_a)
                # ab, branch
                if chr + sub[0] <= "26":
                    if len(sub) > 1:
                        if sub[1] == ',':
                            sub_b = chr + sub
                            ret_str.append(sub_b)
                    else:
                        sub_b = chr + sub
                        ret_str.append(sub_b)
            return ret_str

        if lst == '0' or lst[0] == '0':
            return 0
        if len(lst) == 1:
            return 1
        reversed_lst = lst[::-1]
        stack = []
        print(reversed_lst)
        for chr in reversed_lst:
            ret_str = back_trace(chr, stack)
            if ret_str == 0:
                return 0
            stack = ret_str
        print(stack)
        print('The size of stack =', len(stack))
        b = set(stack)
        print('The size of stack =', len(b))
        return len(b)

    def calculate_total_nums(self, lst):
        def calculate(chr, )

if __name__ == "__main__":
    s = Solution()
    lst = "89451675712132521"
    import pdb; pdb.set_trace()
    count = s.num_decoding(lst)
    print('The count =', count)