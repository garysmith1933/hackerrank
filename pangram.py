def pangrams(s):
    letter_count = [0] * 26
    
    for char in s:
        if char == " ":
            continue
            
        pos = ord(char.lower()) - ord("a")
        print(pos)
        letter_count[pos] += 1
    
    for count in letter_count:
        if count < 1:
            return "not pangram"
    
    return "pangram"
