#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.

def romanToInt(s: str) -> int:
    numerals = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1} # dict for numeral values
    total = 0 # integer value to be returned
    
    i = 0
    while i < len(s)-1:
        if numerals[s[i]] < numerals[s[i+1]]:
            total -= numerals[s[i]]
        else:
            total += numerals[s[i]]
        i+=1
    total += numerals[s[-1]]
    return total

print(romanToInt('MCMXCIV'))


