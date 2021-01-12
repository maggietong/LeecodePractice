"""
stack test for studying
1. expression
    使用栈计算中缀表达式的结果。表达式只含有数字（0-9）和加减乘除符号
    3+2*6-2 = 11
    步骤：
    1.遍历表达式
    2.如果是数字，直接入数栈
    3.如果是符号:
        3.1.若当前符号栈为空，则直接入栈
        3.2.若当前符号栈有操作符，就比较
            a.若当前操作符 优先级<=栈顶操作符，则pop出两个数，pop1个操作符，进行运算，结果入数栈，当前操作符入符号栈
            b.若当前操作符 优先级>栈顶操作符，则当前操作符入符号栈
    4.表达式扫描完毕，中缀表达式就转换成了后缀表达式并存在了数字栈中，下一步就是计算后缀表达式
    5. 从左到右按队列的顺序扫表后缀表达式，如果是数字直接入新的数字栈，如果是符号，从数字栈中取出左右操作数，
    计算表达式并把结果压回数字栈中、就顺序从符号栈和数字栈pop，并运算，结果push进数栈
    最后在数栈中只有一个数字，就是表达式的结果
2. 改进方法是：
先把中缀表达式转换为后缀表达式，然后扫描后缀表达式计算结果就可以
"""
class ObjCls(object):
    def __init__(self, name='', val=''):
        self.name = name
        self.moid = None
        self.val = val

    def say_hi(self):
        print('Hello')

    def do_sth(self):
        print('eating')


class Item(object):
    def __init__(self, item=''):
        self.item = item
        self.next = None

class StackofItem(object):
    def __init__(self, cls_name='ObjCls'):
        self.head = None

    def push(self, obj):
        #        if not isinstance(obj, ObjCls):
        #            raise Exception('The item {0} is not compatible with ObjCls'.format(obj))
        node = Item(item=obj)
        node.next = self.head
        self.head = node

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print('The stack is empty')
            return None
        else:
            node = self.head
            self.head = self.head.next
        return node.item

class CalExpr(object):
    def __init__(self):
        pass

    def get_priority(self, opers):
        if opers == '*' or opers == '/':
            return 2
        if opers == '+' or opers == '-':
            return 1

    def cal_expr(self, left_num, right_num, chr):
        if chr == '+':
            return left_num + right_num
        if chr == '-':
            return left_num - right_num
        if chr == '*':
            return left_num * right_num
        if chr == '/':
            return left_num // right_num

    def print_stack(self, stack):
        head = stack.head
        while head != None:
            print(head.item)
            head = head.next

    def calculate(self, strs):
        strs = strs[::-1]
        num_stack = StackofItem()
        oper_stack = StackofItem()
        opers = ['*', '/', '+', '-']
        i = 0
        while i < len(strs):
            chr = strs[i]
            if chr not in opers:
                j = i
                while j < len(strs):
                    if '0' <= strs[j] <= '9':
                        j = j + 1
                    else:
                        break
                pstr = strs[i:j]
                pstr = pstr[::-1]
                num_stack.push(int(pstr))
                i = j - 1
            else:
                if oper_stack.is_empty():
                    oper_stack.push(chr)
                else:
                    pre_oper = oper_stack.pop()
                    if self.get_priority(chr) >= self.get_priority(pre_oper):
                        oper_stack.push(pre_oper)
                        oper_stack.push(chr)
                    else:
                        pp_oper= oper_stack.pop()
                        sub_str = ''
                        while self.get_priority(pre_oper) <= self.get_priority(pp_oper):
                            left_num = num_stack.pop()
                            right_num = num_stack.pop()
                            val = self.cal_expr(left_num, right_num, pre_oper)
                            num_stack.push(val)
                            pre_oper = pp_oper
                            pp_oper = oper_stack.pop()
                        oper_stack.push(pp_oper)
                        left_num = num_stack.pop()
                        right_num = num_stack.pop()
                        val = self.cal_expr(left_num, right_num, pre_oper)
                        num_stack.push(val)
                        oper_stack.push(chr)
            i = i + 1
        self.print_stack(num_stack)
        self.print_stack(oper_stack)
        while not oper_stack.is_empty():
            left = num_stack.pop()
            right = num_stack.pop()
            oper = oper_stack.pop()
            val = self.cal_expr(left, right, oper)
            num_stack.push(val)
        total = num_stack.pop()
        return total

    def calculate_comp(self, strs):
        stack = StackofItem()
        for chr in strs:
            if chr != ')':
                stack.push(chr)
            else:
                sub_str = ''
                while stack.head.item != '(':
                    sub_str = stack.pop() + sub_str
                stack.pop()
                ret_val = self.calculate(sub_str)
                stack.push(str(ret_val))
                self.print_stack(stack)
        sub_str = ''
        import pdb; pdb.set_trace()
        while not stack.is_empty():
            sub_str = stack.pop() + sub_str
        ret_val = self.calculate(sub_str)
        return ret_val

    def calculate_houzhui(self, strs):
        nmlst = list()
        oplst = list()
        opers = ['+', '-', '*', '/', '(', ')']
        i = 0
        while i < len(strs):
            chr = strs[i]
            if '0' <= chr <= '9':
                j = i
                while j < len(strs):
                    if '0'<=strs[j]<='9':
                        j = j + 1
                    else:
                        break
                nmlst.append(int(strs[i:j]))
                i = j - 1
            else:
                if (oplst == []) or (strs[i] == '('):
                    oplst.append(strs[i])
                elif strs[i] == ')':
                    pre_oper=oplst.pop()
                    while pre_oper != '(':
                        nmlst.append(pre_oper)
                        pre_oper = oplst.pop()
                else:
                    pre_oper = oplst.pop()
                    if pre_oper == '(':
                        oplst.append(pre_oper)
                        oplst.append(chr)
                    elif self.get_priority(chr) >= self.get_priority(pre_oper):
                        oplst.append(pre_oper)
                        oplst.append(chr)
                    else:
                        nmlst.append(pre_oper)
                        oplst.append(chr)
            i = i+1
        while oplst != []:
            op = oplst.pop()
            nmlst.append(op)
        print(nmlst)
        # calculate the total
        tstack = []
        for ele in nmlst:
            if ele not in opers:
                tstack.append(ele)
            else:
                right = tstack.pop()
                left = tstack.pop()
                val = self.cal_expr(left, right, ele)
                tstack.append(val)
        total = tstack.pop()
        print(total)
        return total

if __name__ == "__main__":
    #  sone = StackofItem(cls_name='ObjCls')
    #  a = ObjCls('a', 1)
    #  b = ObjCls('b', 100)
    #  sone.push(a)
    #  sone.push(b)
    #  while not sone.is_empty():
    #      t = sone.pop()
    #      print(t.name, t.val)
    strs = "3-18+3+16/2*3+1"
    strs = '21*((2+3*3-1)+5)+1'
    s = CalExpr()
    import pdb; pdb.set_trace()
    #print(s.calculate(strs))
    #strs = "5*(5*12-3)-100*2+((((3-18+3+16/2*3+1)*5+3)*12)*2-100)"
    #print(s.calculate_comp(strs))
    print(s.calculate_houzhui(strs))
