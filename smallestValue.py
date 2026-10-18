#using list . T.C->O(n*n) when k = n

# def smallest(num: str, k: int) -> str:
#     digits = list(num)
    
#     while k > 0:
#         i = 0
#         found = False
        
#         # Pehla peak element dhoondho
#         while i < len(digits) - 1:
#             if digits[i] > digits[i + 1]:
#                 digits.pop(i)
#                 found = True 
#                 break
#             i += 1
            
#         # Agar koi peak nahi mila (array already sorted hai jaise "12345" ya "9")
#         if not found:
#             digits.pop()
            
#         k -= 1

  
#     res = "".join(digits).lstrip('0')
#     return res if res else "0"


# print(smallest("1432219",3))
# print(smallest("10200",1))
# print(smallest("10",2))



def smallest(num: str, k: int) -> str:
    digits = list(num)
    stack = []
    i=0   

   
    while i < len(digits):
        while k > 0 and stack  and stack[-1]>digits[i]:
            stack.pop()
            k-=1
        stack.append(digits[i])
        i+=1
    
    while k > 0:
        stack.pop()
        k-=1


    res= "".join(stack).lstrip("0") 
    return res if res else "0"



       
print('1' > '1')



