# Input number of lines
#Rhombus
lines = int(input("Enter the number of lines for the rhombus: "))

for i in range(lines):
    print(" " * (lines - i - 1), end="")
    if i == 0 or i == lines - 1:
        print("* " * lines)
    else:
        print("*" + " " * (2 * lines - 3) + "*")
