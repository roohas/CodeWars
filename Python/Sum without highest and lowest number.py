def sum_array(arr):
    #your code heredef sum_array(arr):
    if arr == None or len(arr) == 1:
        return 0
    else:
        arr.sort()
        arr = arr[1:-1]
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return sum