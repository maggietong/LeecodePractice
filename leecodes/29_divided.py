class Solution(object):
    def divide(self, dividend, divisor):
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign:
            result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31) -1

if __name__ == "__main__":
    stra = 9
    strb = 2
    s = Solution()
    import pdb; pdb.set_trace()
    bias = s.divide(stra, strb)
    print(bias)


