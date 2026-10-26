class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i in range(len(nums)):
            val = nums[i]
            if val!=i:
                if ans == -1:
                    ans = val
                else:
                    ans &= val
        
        if ans == -1:
            return 0
        return ans  

class Solution:

  def maxK(self, nums: list[int]) -> int:
    ans = -1  # Binary mein all 1s (masking ke liye identity)

    for i, val in   (nums):
      # Agar element apni sahi sorted position par nahi hai
      if val != i:
        if ans == -1:
          ans = val
        else:
          ans &= val

    # Agar array already fully sorted thi (koi element misplaced nahi tha)
    if ans == -1:
      return 0

    return ans

