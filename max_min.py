def maxMin(k, arr):
    arr.sort()
    
    min_unfair = float('inf')
    
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        
        min_unfair = min(min_unfair, unfairness)
        
    return min_unfair
