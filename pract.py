

def sum(num):
    t_sum = 0
    n = abs(num)
    while n>0:
        t_sum+= n%10
        n = n // 10
    return t_sum      

print(sum(-123))     



sign = -1 if n<0 else 1
rev = 0
n = abs(n)
while n>0:
    ldigit = n %10
    rev = rev*10 + ldigit
    n = n//10

    return sign * rev 