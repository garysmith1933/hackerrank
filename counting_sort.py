def countingSort(arr):
    res = [0] * 100

    for num in arr:
        res[num] += 1
    
    return res
