
# def moveZeroes(nums):
#     n = len(nums)
#     i=0
#     j=0
#     while(j<n):
#         if(nums[j]!=0):
#             nums[i],nums[j] = nums[j],nums[i]
#             i+=1
#         j+=1    
       
           
#     return nums        


# print(moveZeroes([0,1,0,3,12]))
# print(moveZeroes([2]))
# print(moveZeroes([1,0,1]))




# brute force , T.C ,S.C-> O(n)
def moveZeroesBruteForce(nums):
    n = len(nums)
    temp = []
  
    for x in nums:
        if x != 0:
            temp.append(x)
            
 
    while len(temp) < n:
        temp.append(0)
        
  
    # for i in range(n):
    #     nums[i] = temp[i]
        
    return temp

print(moveZeroesBruteForce([0,1,0,3,12]))




# def moveZeroes(num):
#     n = len(num)
#     i=0
   
#     for j in range(n):
#         if num[j]!=0:
#             num[i],num[j]=num[j],num[i]
#             i+=1
#     return num      


# print(moveZeroes([0,1,0,3,12]))