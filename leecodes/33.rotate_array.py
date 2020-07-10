# 33. 搜索旋转排序数组
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
class Solution(object):
    def __init__(self):
        pass

    def is_sequence_array(self, arr, target):
        arr = arr
        def recurse_array(start, end):
            if end - start < 0:
                return -1
            if end - start == 0:
                if target == arr[start]:
                    return start
                else:
                    return -1
            if end-start < 2:
                if target == arr[start]:
                    return start
                elif target == arr[end]:
                    return end
                else:
                    return -1
            lens = end - start + 1
            half = lens // 2
            if target < arr[start]:
                return -1
            elif arr[start] <= target <= arr[half]:
                return recurse_array(start, half)
            elif arr[half] <= target <= arr[end]:
                return recurse_array(half+1, end)
            else:
                #target > arr[end]:
                return -1

        def recurse_rotated_array(start, end):
            if end - start < 0:
                return -1
            if end - start == 0:
                if target == arr[start]:
                    return start
                else:
                    return -1
            if end-start < 2:
                if target == arr[start]:
                    return start
                elif target == arr[end]:
                    return end
                else:
                    return -1
            while start < end:
                lens = end - start + 1
                half = lens // 2
                half = start + half

                # left sequential arr, right not-sequential arr
                if arr[half+1] > arr[end]:
                    if arr[start]<=target<= arr[half]:
                        end = half
                    else:
                        start = half+1
                elif arr[start] > arr[half]:
                    # left non-sequential arr, right sequential arr
                    if arr[half+1] <= target <= arr[end]:
                        start = half+1
                    else:
                        end = half
                else:
                    # left sequential arr, right sequential arr
                    if  arr[start] <= target <= arr[half]:
                        end = half
                    elif arr[half+1] <= target <= arr[end]:
                        start = half+1
                    else:
                        return -1

                # non sequential arr_

        ret = recurse_rotated_array(0, len(arr)-1)
        return ret

if __name__ == "__main__":
    s = Solution()
    lst = [ 7, 9, 11, 23, 56, 78,99, 111, 2,3, 5]
    target = 11
    import pdb; pdb.set_trace()
    ret = s.is_sequence_array(lst, target)
    print(ret)




