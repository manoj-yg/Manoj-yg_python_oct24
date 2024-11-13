def get_minimum_coins(amount,denominations):
    denominations.sort(reverse=True)
    number_of_coins=0
    n=len(denominations)
    i=0
    while amount>0:
        number_of_coins+=amount
        amount=amount%denominations[i]
        i+=1

    return number_of_coins

print(get_minimum_coins(88,[1,2,3,20]))