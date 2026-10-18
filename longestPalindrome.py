def longestPalindrome(s:str)->str:
    n = len(s)
   
    max_length = 0
    start = 0 

    for i in range(n):
        left = i
        right = i

        while left >=0 and right < n:
            
            if s[left]==s[right]:
                curr_length = right - left + 1
                if curr_length > max_length:
                    max_length = curr_length
                    start = left
            else:
                break    

            left-=1
            right+=1

        left,right = i,i+1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                curr_length = right - left + 1
                if curr_length > max_length:
                    max_length = curr_length
                    start = left
            else:
                break
            left-=1
            right+=1            
    
    return s[start:start+ max_lengthlength]
    







