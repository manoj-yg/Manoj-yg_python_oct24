def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input("Enter the value of N: "))

count = 0
num = 2
while count < N:
    if is_prime(num):
        count += 1
    if count == N:
        print(f"The {N}th prime number is: {num}")
    num += 1
