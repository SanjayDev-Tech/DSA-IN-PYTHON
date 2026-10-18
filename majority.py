#Brute force -O(n^2)

# def majorityElement(num):
#     n = len(num)
#     for i in range(n):
#        curr_element = num[i]
#       
#        for j in range(n):
#            if num[j]==curr_element:
#                count += 1
               
#        if count > n//2:
#                 return curr_element
              
    
# print(majorityElement([2,3,3,2]))    

# using sorting alogorithm 
# def majorityElement(num):
#     n = len(num)
#     num.sort()

#     return num[n//2]

# print(majorityElement([2,3,3])) 


# def majorityElement(num):
#     n = len(num)
#     dict = {}

#     for num in num:
#         if num in dict:
#             dict[num]+=1
#         else:
#             dict[num]=1

#         if dict[num] > n // 2:
#             return num     

# print(majorityElement([2,3,3]))  


# def majorityElement(nums):
#     majority = None
#     votes = 0
#     for i in range(len(nums)):
#         if(votes == 0):
#             majority = nums[i]
#             votes=1
#         elif(nums[i]==majority):
#             votes+=1
#         else:
#             votes-=1        
           
#     return majority

# print(majorityElement([3,3,2]))            



def majority(num):
    
    for i in num:
        candidate = i
        count  = 0

        for j in range(len(num)):
            if num[j]==candidate:
                count+=1
        if count > len(num)//2: 
            return candidate

print(majority([2,2,1,1,1,1,2,2]))         






    
 

