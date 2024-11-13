number1 = 15
number2 = 25.5

print(f"type of number1 = {type(number1)}")  # <class 'int'>
print(f"type of number2 = {type(number2)}")  # <class 'float'>

print(f"Bit count of number1 = {number1.bit_count()}")

print(f"Size of number1 in memory = {number1.__sizeof__()} bytes")

print(f"Does number1 equal 15? {number1.__eq__(15)}")