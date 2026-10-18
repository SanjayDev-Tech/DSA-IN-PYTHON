# def totalMoney(n: int) -> int:
#     total_money = 0
#     curr_amt = 1
#     monday_amt = 1

#     for i in range(n):
#         total_money+= curr_amt
#         curr_amt+=1

#         if (i+1) % 7==0:
#             monday_amt+= 1
#             curr_amt= monday_amt

       
        
#     return total_money  


# print(totalMoney(10))      







# total_money = 0
# curr_amt = 1
# monday_amt = 1

# for i in range(10):
#     total_money += curr_amt
#     curr_amt+=1

#     if((i+1)%7==0):
       
#         monday_amt+=1
#         curr_amt = monday_amt 
    


# print(total_money)


def totalMoneyWithWeekend(n: int) -> int:
    total_amt = 0
    monday_amt = 1
    curr_amt = 1

    for i in range(n):
        if i%7==5 or   i%7==6:
            total_amt += 2* curr_amt
        else:
            total_amt+=curr_amt

        curr_amt+=1        
       
       
        if (i+1)%7==0:
            monday_amt+=1
            curr_amt= monday_amt

    return total_amt 


print(totalMoneyWithWeekend(7))            










      



