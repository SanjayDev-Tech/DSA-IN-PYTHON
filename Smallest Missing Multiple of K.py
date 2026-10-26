#Bruteforce T.c-> O(M*N)
# def missingMultiple(num,k):
#     i=1
#     while True:
#         multiple = k * i

#         if multiple not in nums:
#             return multiple   
#         i+=1 

#using set T.c-> O(N)  
def missingMultiple(num,k):
    num_set = set(num)
    i=1
    while True:
        multiple = k * i

        if multiple not in num_set:
            return multiple   
        i+=1 



def missingMultiple(num,k):
    num.sort()
    target = k

    for n in mum:
        if n == target:
            target+=k
        else:
            if n > target:
                break

    return target            


def missingMultiple(nums,k)->int:
    num_set = set(nums)
    i = 1
    while True:
        multiple = k * i
        if multiple not in num_set:
            return multiple
        i+=1
