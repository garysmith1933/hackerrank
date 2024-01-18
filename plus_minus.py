
def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            pos_count += 1
        
        elif num < 0:
            neg_count += 1
        
        else:
            zero_count += 1
    
    pos_ratio = f"{pos_count / len(arr):.6f}"
    neg_ratio = f"{neg_count / len(arr):.6f}"
    zero_ratio = f"{zero_count / len(arr):.6f}"
            
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)
