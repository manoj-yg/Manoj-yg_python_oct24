# Input number
#check the number is palindrome
number = input("Enter a number: ")

# Check if the number reads the same forwards and backwards
if number == number[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
