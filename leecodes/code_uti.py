class Solution(object):
    def __init__(self):
        pass

    def do_task(self, S):
    if S=='':
        return 0
    N = len(S)
    if N<7:
        return 0
    stand_lst = [1,1,2,2,1]
    dic_s = {
        'B':0,
        'A': 0,
        'L': 0,
        'O': 0,
        'N': 0
    }
    for a in S:
        if a in dic_s.keys():
            dic_s[a] += 1
    print(dic_s)
    lst_cnt = list(dic_s.values())
    print(lst_cnt)
    ret_1 = min(lst_cnt[0], lst_cnt[1], lst_cnt[4])
    ret_2 = min(lst_cnt[2], lst_cnt[3])
    if ret_2 >= (ret_1*2):
        ret = ret_1
    else:
        ret = ret_2 // 2
    return ret

if __name__ == "__main__":
    #S = "BAONXXOLL"
    #S ="BAOOLLNNOLOLGBAX"
    S="QAWABAWONL"
    S = "ABC"
    balllon = "BALLOON"
    s = Solution()
    ret = s.do_task(S,s)
    print(ret)