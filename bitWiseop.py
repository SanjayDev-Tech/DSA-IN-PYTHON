def max_value(n,k):
    max_and = 0
    max_or = 0
    max_xor = 0

    for i in range(1,n):
        for j in range(i+1,n+1):
            curr_and = i & j
            curr_or  = i | j
            curr_xor = i ^ j

            if(curr_and > max_and and curr_and < k):
                max_and = curr_and
            if (curr_or > max_or and curr_or <k):
                max_or = curr_or   
            if (curr_xor > max_xor and curr_xor <k):
                max_xor = curr_xor 

    return max_and,max_or,max_xor

ans_and ,ans_or,ans_xor = max_value(5,4)    
print(ans_and)
print(ans_or)
print(ans_xor)