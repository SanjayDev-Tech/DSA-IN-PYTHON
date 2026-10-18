# def rotateArray(num,k):
#     n = len(num)
#     k = k%n
#     temp = [0]*n
#     for i in range(n):
#         temp[(i+k)%n] = num[i]

#     return temp


# print(rotateArray([1,2,3,4],6))

# class Solution:
#     def rotateArray(self,num: list[int], k: int)->None:

#         n = len(num)
#         k = k%n  
        
#         def reverse(left:int ,right: int)->None:   
#             while(left < right):
#                 num[left],num[right]=num[right],num[left]
#                 left+=1
#                 right-=1

#         reverse(0,n-1)

#         reverse(0,k-1)

#         reverse(k,n-1)

# my_nums = [1, 2, 3, 4, 5, 6, 7]
# k_value = 3
# obj =Solution()
# obj.rotateArray(my_nums,k_value)  #call by reference


# print("roated array:" ,my_nums)






# def rotateArray(num,k):
#     n=len(num)
#     k=k%n
#     temp = [0]*n
#     for i in range(n):
#         temp[(i+k)%n] = num[i]

#     num[:] = temp 
#     return num    

# print(rotateArray([1,2,3,4],2))




# def sortedrotated(num):
#     n =len(num)
#     count =0
#     for i in range(n):
#         if(num[i])



# num.reverse()

# nums[:k]  = reversed(nums[:k])



#inserting multiple elements at index and expand list 
# nums = [1, 2, 3]
# nums[2:2] = [10, 20]

# print(nums)


# import sys

# # Maximum value representable by a signed word (pointer size)
# print(sys.maxsize)



# def rotate_array(num,k):
#     n = len(num)
#     def reverse(left,right):
        
#         while left < right:
#             num[left],num[right] = num[right],num[left]
#             left+=1
#             right-=1


#     reverse(0,n-1)
#     reverse(0,k-1)
#     reverse(k,n-1)

#     return num

# print(rotate_array([1,2,3,4,5,6],3))



# def isrotated(num)->bool:
#     n = len(num)
#     count = 0
#     for i in range(n):
#         if num[i]>num[(i+1)%n]:
#             count+=1
#     return count <=1
# print(isrotated([2, 1, 3, 4]))            
            



def is_rotated(arr1,arr2):
    if len(arr1) != len(arr2):
        return False

    if not arr1:
        return True    

    n = len(arr1)
    first_element = arr1[0]

  
    for i in range(n):
        if arr2[i] == first_element:
            start_idx = i  
            match_found = True
         
            for j in range(n):
                if arr1[j] != arr2[(start_idx + j)%n]: 
                    match_found = False 
                    break

            if match_found:
                return True
        
    return False



print(is_rotated([1,2,1,3],[1,3,2,1]))
