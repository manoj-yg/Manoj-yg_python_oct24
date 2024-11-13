#print to check if a number is Even or odd

print("Enter a number to check if it is Even: ")
input_num=int(input())

if input_num % 2 == 0:
    print('Input number',input_num,'is Even')
else:
    print("Input number",input_num,'Is odd')