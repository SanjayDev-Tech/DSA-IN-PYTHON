#Brute force 
# def frequentEven(nums):
#     n = len(nums)
#     ans=-1
#     frequency = 0

#     for i in range(n):
#         curr_element = nums[i]
#         count = 0

#         if curr_element%2!=0:
#             continue
 
#         for j in range(n):
#             if nums[j] == curr_element:
#                 count+=1

#         if count>frequency:
#                 frequency = count
#                 ans = curr_element
#         elif count == frequency and curr_element<ans:
#                 ans = curr_element

#     return ans     

        
# print(frequentEven([0, 4, 2, 2, 4, 4, 1])) 


#using dict .T.C->O(n) S.C->O(n)
def frequentEven(nums):
    n = len(nums)
    ans=-1
    frequency = 0
    my_dict = {}

    for num in nums:
        if num%2!=0:
            continue

        if num in my_dict:
              my_dict[num]+=1
        else:
              my_dict[num] = 1      
        

        if my_dict[num]>frequency:
                frequency = my_dict[num]
                ans = num
        elif my_dict[num] == frequency and num < ans:
                ans = num

    return ans   

print(frequentEven([0, 1, 2, 2, 4, 4, 1])) 