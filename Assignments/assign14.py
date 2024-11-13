#Print Nth Digit of a Number (Starting from Right)
# Input number and position
number = input("Enter a number: ")
N = int(input("Enter the position from the right: "))

# Get the Nth digit from the right
if 1 <= N <= len(number):
    print(f"The {N}th digit from the right is: {number[-N]}")
else:
    print("Position out of range.")
