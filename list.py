# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/P5Bt1phtMNo

# Empty list:
new_list = []
new_list_2 = list()

# Initialize list
my_list = [1, 2, 3, 4, 5]
# fruits = ["apple", "banana"]
# mixed_list = [1, "apple", True, {"name": "Shubham"}, ["coding", "content creation"]]

# Access list
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
sublist = my_list[1:4]

# Appending Elements
my_list.append(6)
my_list.append(6) # Duplicate values allowed

# Extending List
my_list.extend([7, 8, 9])

# Inserting Element at a Specific Index
my_list.insert(2, 10)

# Removing Element by Value
my_list.remove(3)

# Popping Element by Index
popped_element = my_list.pop(4)

# Finding Index of Element
index_of_5 = my_list.index(5)

# Checking if Element is in List
is_present = 7 in my_list

# Counting Occurrences
count_of_2 = my_list.count(2)

# Sorting in Place
my_list.sort()

# Reversing in Place
my_list.reverse()

# Copying a List
new_list = my_list.copy()

# Clearing a List
my_list.clear()

# List Comprehension
squared = [x**2 for x in my_list]

# Concatenating Lists
concatenated_list = my_list + [11, 12, 13]

# Length of List
length_of_list = len(my_list)

# Access each element
for i in my_list:
    print(i)
