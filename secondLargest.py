
# def SecondLargest(nums):
#     largest = float('-inf')
#     slargest = float('-inf')
#     n = len(nums)
#     if n<2:
#         return -1
#     for i in range(n):
#         if nums[i]>largest:
#             slargest = largest
#             largest = nums[i]

#         elif slargest<nums[i] and nums[i] != largest:
#             slargest = nums[i]   

#     return slargest


# # print(SecondLargest([5,7,10,8,9]))
# # print(SecondLargest([8,9,9]))
# print(SecondLargest([8]))


class Solution:
    def Secondsmallest(self, nums:list[int])->int:
        smallest = float("inf")
        ssmallest = float("inf")

        n = len(nums)
        if n<2:
            return -1
        for i in range(n):
            if nums[i]<smallest:
                ssmallest = smallest
                smallest = nums[i]

            elif nums[i]<ssmallest and nums[i]!=smallest:
                ssmallest = nums[i]

        return ssmallest if ssmallest != float("inf") else -1

obj= Solution()
# print(obj.Secondsmallest([2,5,3]))
print(obj.Secondsmallest([2,2,2]))


          






# lar = float('inf')
# s_lar = float('-inf')  

# if n<2:
#     return -1

# for i in range(n):
#     if a[i]>lar:
#         s_lar = lar
#         lar = a[i]
#       
#     elif a[i]<lar and s_lar < a[i]:
#         s_lar= a[i]




def Smallest(num):
    small = num[0]
    s_s = -1

    for i in range (1,len(num)):
        if num[i]<small:
            s_s = small
            small = num[i]
         
        elif num[i] < s_s and num[i] > small :
            s_s = num[i]    

    return s_s


print(Smallest([4,1,2,3]))
