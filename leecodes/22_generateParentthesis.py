class Solution(object):
    def generateParentthesis(self, n):
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str:
            :param left: the remain left parenthesis
            :param right: the remian right parenthesis
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                pass
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right-1)

        dfs(cur_str, n, n)
        return res