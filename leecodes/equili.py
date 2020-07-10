def solution(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return -1
    if arr_len == 1:
        return 0
    p_lst = []
    for p in range(arr_len):
        sum_left = 0
        sum_right = 0
        for i in range(p):
            sum_left += arr[i]
        for j in range(p+1,arr_len):
            sum_right += arr[j]
        if sum_left == sum_right:
            p_lst.append(p)

    return p_lst

if __name__ == "__main__":
    arr = [-1, 3, -4, 5, 1, -6, 2, 1]
    ret = solution(arr)
    print(ret)