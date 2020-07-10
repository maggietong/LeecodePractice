"""
计算两个超大的数的乘积，其中任何一个都有可能超过计算机的最大表示数，
思考思路是：
大数可以用字符数组表示，把两个数的乘积转换成加法运算，把其中一个较小的大数拆分成一位位的个位数，
然后个位数分别于大数相乘，相乘之后的乘积再相加，这个要考虑到百位的各位数要乘以100， 千位的个位数要乘以1000，也就是字符数组后添加"000"
其中个位数与大数相乘，也就是一个单位数与大数的字符数组相乘的计算，可以先计算各个位数相乘的乘积，然后得到一个每位数相乘的乘积数组，
然后考虑进位的问题，进位计算可以用除以10取整得到进位值，取余得到该位值，然后把乘积数组考虑进位后合成一个字符数组，两个计算连个字符数组的和
"""
class Test(object):
    def __init__(self):
        self.total = "0"
        self.stra = "0"
        self.strb = "0"

    def __repr__(self):
        print('Test Class')
        print(self.stra, ' * ', self.strb, '=', self.total)

    def multiply(self, stra, strb):
        """
        :param stra: 输入的字符串
        :param strb: 输入的字符串
        :return: 返回相乘后的字符串
        """
        self.stra = stra
        self.strb = strb
        if stra == "0" or strb == "0":
            self.total = "0"
            return self.total
        n = 0
        strb = strb[::-1]
        for digit in strb:
            #一位数字与一个大数串的乘积
            part_total = self.sigle_digit_multiply(int(digit), stra)
            part_total = part_total + '0' *n
            n += 1
            #两个字符串相加
            self.total = self.twostrings_plus(self.total, part_total)

        return self.total

    def sigle_digit_multiply(self, digit, stra):
        str_val = []
        stra = stra[::-1]
        for i, char in enumerate(stra):
            num = int(char)
            str_val.append(num * digit)
        print(str_val)
        #得到每一位的数与一个数的乘积数组，考虑进位，得到一个单位数与大数的乘积的字符串表示
        str_val = self.carry_deal(str_val)
        str_val = str_val[::-1]
        return "".join(str(i) for i in str_val)

    def carry_deal(self, str_val):
        i = 0
        while i < len(str_val):
            if str_val[i] >= 10:
                #取整得到进位
                carrier = str_val[i] // 10
                if i == len(str_val) - 1:
                    str_val.append(carrier)
                else:
                    str_val[i+1] += carrier
                #取余得到该位的值
                str_val[i] = str_val[i] % 10
            i += 1

        return str_val

    def twostrings_plus(self, stra, strb):
        if len(stra) < len(strb):
            stra, strb = strb, stra
        lsta = [int(i) for i in stra]
        lstb = [int(i) for i in strb]
        #从各位数开始计算，'456' + '789'，所以要从字符串最后开始
        lsta = lsta[::-1]
        lstb = lstb[::-1]
        for i, digit in enumerate(lstb):
            lsta[i] += lstb[i]

        #得到了每位相加之后的数组列表，考虑进位问题转换为一个大数字符串
        lsta = self.carry_deal(lsta)
        lsta = lsta[::-1]
        return "".join(str(i) for i in lsta)


if __name__ == '__main__':
    stra = "12345"
    strb = "678"
    s = Test()
    import pdb; pdb.set_trace()
    s.carry_deal(str_val =[40, 32, 24, 16, 8])
    s.twostrings_plus('456', '789')
    total = s.multiply(stra, strb)
    print("stra=", stra)
    print("strb=", strb)
    print("multiply_total=", total)