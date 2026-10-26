#T.C  -> o(N) S.C->O(1)
def  firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):

        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            valid_idx = nums[i] - 1
            nums[i],nums[valid_idx] = nums[valid_idx],nums[i]

    for i in range(n):
        if nums[i]!=i+1:
            return i+1    

    return n+1 


def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
    num_set = set(nums)
       

    res = []
       

    for i in range(1,len(nums)+1):
        if i not in num_set:
            res.append(i)
            
     
    return res         



#without extra space o(1)

n = len(nums)

for i in range(n):
    while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
        valid_idx = nums[i] - 1
        nums[i],nums[valid_idx] = nums[valid_idx],nums[i]


    res = []
    

