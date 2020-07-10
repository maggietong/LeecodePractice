'''
38. 外观数列
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。
'''
class Solution(object):
    def __init__(self):
        pass

    def print_n_list(self, N):
        def cal_up_list(n):
            if n == 1:
                return '1'
            if n>1:
                rs = cal_up_list(n-1)
                if len(rs) == 1:
                    return '11'
                if len(rs) == 2:
                    if rs[0] == rs[1]:
                        ret_rs = '2'+rs[0]
                    else:
                        ret_rs = '1'+rs[0]+'1'+rs[1]
                    return ret_rs
                i = 0
                ret_rs = ''
                while i<len(rs):
                    cont = 1
                    if i == (len(rs) -2):
                        if rs[i] == rs[i+1]:
                            ret_rs = ret_rs + '2' + rs[i]
                        else:
                            ret_rs = ret_rs + '1' + rs[i] + '1' + rs[i+1]
                        return ret_rs
                    if i == len(rs) - 1:
                        ret_rs = ret_rs + '1' + rs[i]
                        return ret_rs

                    if rs[i] == rs[i+1]:
                        if (rs[i] == rs[i+2]):
                            cont += 2
                            ret_rs = ret_rs + str(cont) + rs[i]
                            i += 3
                        else:
                            cont += 1
                            ret_rs = ret_rs + str(cont) + rs[i]
                            i += 2
                    else:
                        ret_rs = ret_rs+str(cont)+rs[i]
                        i += 1
                return ret_rs
        ret = cal_up_list(N)
        return ret

if __name__ == '__main__':
    s = Solution()
    N = 6
    import pdb; pdb.set_trace()
    print(s.print_n_list(N))
