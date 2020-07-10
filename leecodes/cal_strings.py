"""
design a simple calculator
for example:
  ret = "3+((5+3)*2+2)*3+((7-8)*3 -2 + 4) + 5*1"
           23   7    12  16，17，21，28
"""
import copy

class Solution(object):
    def cal_val(self, strs):
        def cal_expr(exp):
            exp = exp.rstrip('(')
            exp = exp.lstrip(')')
            for a in exp:
                if (a>='0') and (a<='9')
                    b = int(a)
                if a == '+':
                    b = +
                if a == "-":
                    b = -
            return 11

        def cal_parenthesis(head, tail):
            start = bra_stack.index(head)
            end = bra_stack.index(tail)
            if end - start == 1:
                return cal_expr(strs[head[1]:tail[1]+1])
            # ((5+3)*2+2)
            sub_str = strs[head[1]:tail[1]+1]
            start = start + 1
            end = end -1
            head = bra_stack[start]
            tail = bra_stack[end]
            if end - start  >= 1:
                # (5+3)
                ret = cal_parenthesis(head, tail)
                ret_str = str(ret)
                sub_str = sub_str.replace(strs[head[1]:tail[1]+1], ret_str)
                #(8*2+2)
                ret_str = cal_expr(sub_str)
                ret_str = str(ret_str)
            return ret_str

        #start to cal the max inner () value
        if len(strs) == 0:
            return False
        if len(strs) == 1:
            return int(strs)

        bra_stack = []
        for i in range(len(strs)):
            if strs[i] == '(' or strs[i] == ')':
                bra_stack.append((strs[i],i))
        if len(bra_stack) == 0:
            return cal_expr(strs)
        # calculate the value of inter-bracket
        tmp_bra_stack = copy.deepcopy(bra_stack)
        tmp_stack = []
        sub_strs = copy.copy(strs)
        for sub in bra_stack:
            a = tmp_bra_stack.pop(0)
            if a[0] == "(":
                tmp_stack.append(a)
            elif a[0] == ")":
                b = tmp_stack.pop()
                if len(tmp_stack) == 0:
                    ret = cal_parenthesis(b, a)
                    sub_strs = sub_strs.replace(strs[b[1]:a[1]+1],ret)
        total = cal_expr(sub_strs)
        return total

if __name__ == "__main__":
    #strs = "1*(2+3)"
    strs = "3+((5+3)*2+2)*3+((7+8)*3+2 + 4)+5*1"
    s=Solution()
    import pdb; pdb.set_trace()
    ret = s.cal_val(strs)
    print(ret)


