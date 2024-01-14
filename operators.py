# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: 


data1 = 5
data2 = 10

# Arithmetic Operators: +, -, *, **, %,/, //
# Addition
total_age = 27 + 4
print(f"Total is: {total_age}")

# Subtraction
total_age = 2024 - 1996
print(f"Subtraction is: {total_age}") 

# multiplication
result = data1 * data2
print(f"Multiplication is: {total_age}")

# division
result = data1 / data2
print(f"Division is: {result}")

# floor division
result = data1 // data2
print(f"Floor Division is: {result}")

# modulo
result = data1 % data2
print(f"Modulo is: {result}")

# a to the power b
result = data1 ** data2
print(f"Power is: {result}")


# Comparison Operators: ==, !=, <, >, <=, >=
is_equal = data1 == data2
print(f"Is data1 equal to data2?: {is_equal}")

# Not equal to
print(f"Result = {data1 != data2}")

# Greater than
print(f"Result = {data1 > data2}")

# Greater than or equal to
print(f"Result = {data1 >= data2}")

# Less than
print(f"Result = {data1 < data2}")

# Less than or equal to
print(f"Result = {data1 <= data2}")


# Logical Operators: and, or, not
is_motivated = True
age = 28

# logical AND
is_young_boy = age <= 30 and is_motivated
print(f"Is young and hungry?: {is_young_boy}")

# Logical OR
print(f"Is young OR hungry?: {is_young_boy}")

# Logical NOT
print(not True)


# Assignment Operators: =, +=, -=, *=, /=
age = 27
print(f"Age is {age}")

age += 1
print(f"New age is {age}")

age -= 1
print(f"New age is {age}")

age *= 2
print(f"Double of the age is {age}")

age /= 2
print(f"Half of the age is {age}")


# Membership Operators: in, not in
list_data = [27, 28, 29, 30]

# In
is_present = age in list_data
print(f"{is_present=}")

# Not in 
is_present = age not in [27,28,29,30]
print(f"{is_present=}")


# Identity Operators: is, is not
new_var = None

# Is
identity_op = new_var is None
print(f"{identity_op=}")

# Is not
identity_op = [4, 27] is not [4, 27]
print(f"{identity_op=}")


# bitwise operators: &, |, ~, ^, <<, >>

a = 10 # => 1010
b = 6  # => 0110
result = a & b
# Result => 0010 => 2
result_or = a | b
# Result => 1110 => 14
print(f'a & b = {result}, {result_or=}')
