def prefix_sum_array(num):
    n = len(num)
    prefix  = [0] * n
    prefix[0] = num[0]

    for i in range(1,n):
        prefix[i]  = prefix[i-1] + num[i]

    return prefix    



