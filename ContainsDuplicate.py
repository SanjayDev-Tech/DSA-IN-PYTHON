#brute force . TC-O(n**2)
# def containsDuplicate(num):
#     n = len(num)
#     for i in range(n):
#         for j in range(i+1,n):
#             if(num[i]==num[j]):
#                 return True
#     return False            
 
# print(containsDuplicate([1,2,3,1]))



def containsDuplicate(num):
    seen = set()
    
    for i in num:
        for i in seen:
            return True
        seen.add(i) 

    return False

print(containsDuplicate([1,2,3,1]))
