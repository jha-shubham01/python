# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/P5Bt1phtMNo

# !Note:
# Tuples are not mutable
# Tuple can have duplicate data

# Empty Tuple:
new_tuple = []
new_tuple_2 = tuple()

# Initialize Tuple
# fruits = ("apple", "banana")
# mixed = ("apple", 1, True, {"name": "Shubham"}, ["coding", "content creation"])
my_tuple = (1, 2, 3, 4, 5, 5)

# Accessing Elements
first_element = my_tuple[0]

# Slicing
sublist = my_tuple[1:4]

# Concatenating Tuples
concatenated_tuple = my_tuple + (6, 7, 8)

# Repeating Tuple Elements
repeated_tuple = my_tuple * 2

# Finding Index of Element
index_of_5 = my_tuple.index(5)

# Checking if Element is in Tuple
is_present = 7 in my_tuple

# Counting Occurrences
count_of_2 = my_tuple.count(2)

# Length of Tuple
length_of_tuple = len(my_tuple)

# Converting to List
tuple_to_list = list(my_tuple)

# Converting to Set
tuple_to_set = set(my_tuple)

# Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))

# Tuple Unpacking
a, b, c = my_tuple

# Checking Equality
is_equal = (1, 2, 3) == (1, 2, 3)

# Creating Single-Element Tuple
single_element_tuple = (10,)