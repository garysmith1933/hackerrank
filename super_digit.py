def superDigit(n, k):
    nums = [int(char) for char in n]
    num = sum(nums) * k

    if num < 10:
        return num
    
    return superDigit(str(num), 1)
