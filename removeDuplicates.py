def removeDuplicates(nums):
    i=0

    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i] = nums[j]


    return i+1          


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))        


# def removeDuplicates(nums):
#     i=2
#     for j in range(2,len(nums)):
#         if nums[j]!=nums[i-2]:
#             nums[i] = nums[j]
#             i+=1

#     return i        

# print(removeDuplicates([1,1,1,2,2,3]))  





# def removeDuplicates(nums):
#     temp = []
#     count = 0

#     for i in range(len(nums)):
#         if i = 0 or nums[i]!= nums[i-1]:
#             count = 1
#         else:
#             count+=1 
#         if count <= 2:
#             temp.append(nums[i])

#     for j in range(len(temp)):
#         nums[j] = temp[j]   


#     return len(temp)         
        


def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    pivot = -1

    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot = i
            break
    if pivot != -1:
        for j in range(n-1,pivot,-1):  
            if nums[j]>nums[pivot]:   
                nums[j],nums[pivot] = nums[pivot],nums[j]
                break       

    nums[pivot + 1 :] = nums[pivot+1:][::-1]           




for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
        pivot = i
        break

for j in range(n-1,pivot,-1):
    if nums[j]>nums[pivot]:
        nums[pivot],nums[j] = nums[j],nums[pivot]
        break







class Solution:

  def nextPermutation(self, nums: list[int]) -> None:
    n = len(nums)
    i = n - 2

    # Step 1: Breakpoint dhoondho (right to left)
    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1

    # Step 2: Agar breakpoint mila, toh just bada element dhoondh kar swap karo
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
       

    # Step 3: Breakpoint ke aage wale descending hisse ko reverse karke ascending banao
    left, right = i + 1, n - 1
    while left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1