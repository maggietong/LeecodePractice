def insertion_sort(a):
    length = len(a)
    if length <=1:
        return 
    for i in range(1,length):
        current = a[i]
        pre_index = i - 1
        while pre_index >= 0 and a[pre_index] > current:
            a[pre_index + 1] = a[pre_index]
            pre_index -= 1
        a[pre_index + 1] = current
    return a

if __name__ == "__main__":
    num = [11, 33,86,36,59,12,51,32,44]
    insertion_sort(num)
    for i in range(len(num)):
        print(num[i])
