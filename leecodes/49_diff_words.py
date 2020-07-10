"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def is_same_diff_words(word_a, word_b):
            if word_a == "" and word_b=="":
                return True
            if word_b == '':
                return False
            if len(word_a) != len(word_b):
                return False
            amap = {}
            bmap = {}
            for i in range(len(word_a)):
                if word_a[i] not in amap.keys():
                    amap[word_a[i]] = 1
                else:
                    amap[word_a[i]] += 1
                if word_b[i] not in bmap.keys():
                    bmap[word_b[i]] = 1
                else:
                    bmap[word_b[i]] += 1
            if amap == bmap:
                return True
            return False

        if len(strs) == 0:
            return 0
        if len(strs) == 1:
            return [[strs[0]]]
        ret_list = [[strs[0]]]
        for sub_strs in strs[1:]:
            flag = 0
            for sub_lst in ret_list:
                if is_same_diff_words(sub_strs, sub_lst[0]):
                    sub_lst.append(sub_strs)
                    flag = 1
                    break
            if flag == 0:
                ret_list.append([sub_strs])
        return ret_list

if __name__ == "__main__":
    #strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    #strs = ["", ""]
    strs = ["cab","pug","pei","nay","ron","rae","ems","ida","mes"]
    s = Solution()
    import pdb; pdb.set_trace()
    ret = s.groupAnagrams(strs)
    print(ret)