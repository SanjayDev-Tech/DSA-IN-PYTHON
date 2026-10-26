#Brute force
def shortestPalindrome(s: str) -> str:
    rev_s = "".join(reversed(s))

    for i in range(len(s)):
        if s.startswith(rev_s[i:]):
                return rev_s[:i] + s

print(shortestPalindrome("abacabaXY"))            

#using KMP ALGO 
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev_s = s[::-1]
        temp = s + "#" + rev_s
        n = len(temp)  
        
        # Step 1: KMP LPS Table construct karo
        lps = [0] * n
        length = 0
        i = 1
        
        while i < n:
            if temp[i] == temp[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        
        longest_pal_len = lps[-1]
        
    
        rem = s[longest_pal_len:]
        return rem[::-1] + s

    


if not s:
    return s


rev = "".join(reversed(s))

temp = s + "#" + rev

n = len(s)

lps = [0] * n
length = 0
i=1

while i < n:
    if temp[i]==temp[length]:
        lenth+=1
        lps[i]= length
        i+=1
    else:
        if length !=0:
            length = lps[length -1]
          
        else:
            i+=1   

    longest_pal_length= lps[-1]

    rem = s[longest_pal_len:]

    return rem[::-1] + s





def shortestPalindrome(s):
    n = len(s)
    rev_s = "".join(reversed(s))
    for i in range(n):
        if s.startswith(rev_s[i:]):
            rem = rev[:i]
    return rem + s        