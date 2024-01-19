def lonelyinteger(a):
    count = {}
    
    for num in a:
        count[num] = count.get(num, 0) + 1
    
    for num in count:
        if count[num] == 1:
            return num
