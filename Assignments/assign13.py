#Print Nth Digit of a Number (Starting from Left)
# Input number and position
number = input("Enter a number: ")
N = int(input("Enter the position from the left: "))

# Get the Nth digit from the left
if 1 <= N <= len(number):
    print(f"The {N}th digit from the left is: {number[N-1]}")
else:
    print("Position out of range.")
