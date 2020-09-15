def find_median(arr):    
    arr = sorted(arr)
    middle = int(len(arr) / 2)
    if len(arr) % 2 == 0:
        median = int(arr[middle] + arr[middle - 1]) / 2
    else:
        median = int(arr[middle])
    return median

print(find_median([2, 10, 19, 1, 14, 16]))
#1, 2, 10, 14, 16, 19