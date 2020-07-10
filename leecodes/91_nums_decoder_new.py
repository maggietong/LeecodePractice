# 91_nums_decoder_new.py
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
        mem_buffer = {}
        def back_trace(lst):
            if lst == '':
                mem_buffer[lst] = 1
                return 1
            if len(lst) == 1:
                if (lst != '0'):
                    mem_buffer[lst] = 1
                    return 1
                else:
                    return 0
            print(lst)
            lst_bak = lst
            chr = lst[0]
            lst = lst[1:]
            pre_chr = lst[0]
            pre_lst = lst[1:]
            #cal_left_branch
            if chr == '0':
                if pre_chr == '0':
                    return 0
                # cal left branch and right branch
                else:
                    if lst in mem_buffer.keys():
                        left_num = mem_buffer[lst]
                    else:
                        left_num = back_trace(lst)
                        mem_buffer[lst] = left_num
                    right_num = 0
            else:
                if pre_chr == '0':
                    left_num = 0
                    if chr+pre_chr > '26':
                        right_num = 0
                    else:
                        if pre_lst in mem_buffer.keys():
                            right_num = mem_buffer[pre_lst]
                        else:
                            right_num = back_trace(pre_lst)
                            mem_buffer[pre_lst] = right_num
                else:
                    if lst in mem_buffer.keys():
                        left_num = mem_buffer[lst]
                    else:
                        left_num = back_trace(lst)
                        mem_buffer[lst] = left_num
                    if (chr+pre_chr) > '26':
                        right_num =0
                    else:
                        if pre_lst in mem_buffer.keys():
                            right_num = mem_buffer[pre_lst]
                        else:
                            right_num = back_trace(pre_lst)
                            mem_buffer[pre_lst] = right_num
            print(mem_buffer)
            print('----')
            total_num = left_num + right_num
            if total_num ==  0:
                return 0
            mem_buffer[lst_bak] = total_num
            return total_num

        # begin to calculate
        if lst == '':
            return 0
        if lst == '0':
            return 0
        if lst[0] == '0':
            return 0
        if '00' in lst:
            return 0
        total_num = back_trace(lst)
        return total_num

if __name__ == "__main__":
    s = Solution()
    lst = "12120"
    import pdb; pdb.set_trace()
    count = s.num_decoding(lst)
    print('The count =', count)