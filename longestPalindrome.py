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
    
    return s[start:start+ max_length]


#count substring

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Helper function jo given center se expand karta hai
        def expand(left: int, right: int) -> int:
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(n):
            count += expand(i, i)      # Odd length expansion
            count += expand(i, i + 1)  # Even length expansion

        return count

