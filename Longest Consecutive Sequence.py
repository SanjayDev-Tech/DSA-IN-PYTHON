

def longestConsecutive(nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            curr_num = num
            if curr_num-1 not in num_set:

                while curr_num+1 in num_set:
                    curr_num+=1 
                length  = curr_num - num + 1
                max_length = max(length,max_length)

        return max_length      


print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


          
            


def waysToBuyPensPencils(total: int, cost1: int, cost2: int) -> int:
  
    ntotal_ways = 0
    num_of_pens = total // cost1 

    for i in range(num_of_pens+1):
        remaining_amount = total - (cost1 * i)
        num_of_pencils = remaining_amount // cost2 +1 
      
      
        total_ways+= num_of_pencils

    return total_ways



