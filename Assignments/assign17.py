# Input number of lines
lines = int(input("Enter the number of lines for the triangle: "))

for i in range(1, lines + 1):
    print(" " * (lines - i) + "* " * i)
# for equilateral triangle