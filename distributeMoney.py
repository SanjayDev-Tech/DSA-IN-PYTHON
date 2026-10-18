 def distMoney(money: int, children: int) -> int:
    if money < children:
        return -1
    
    money = money - children

    count = money//7  #kitne 7-7 ke bundles bne 

    remaining_amt = money % 7        

    if count > children  or (count == children and remaining_amt>0):
        return children -1

    if count == children and remaining_amt ==0:    #here count is like tickets 
        return children


    if remaining_amt==3 and children - count ==1:
        return count -1

    return counts    









