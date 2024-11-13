def is_composite(number):
    # A number is composite if it has divisors other than 1 and itself
    if number <= 1:
        return False  
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True  
    return False 

num = int(input("Enter to check number is composite or not: "))
if is_composite(num):
    print(f"{num} is a composite number.")
else:
    print(f"{num} is not a composite number.")
