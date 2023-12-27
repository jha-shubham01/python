# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/P5Bt1phtMNo

# !Note:
# Sets stores unique data (Duplicate will be removed)
# Sets doesn't have order

# fruits = {"apple", "banana"}
# mixed = {1, "apple", True}
my_set = {1, 2, 3, 4}

# Adding an Element
my_set.add(6)

# Updating with Another Set
my_set.update({7, 8, 9})

# Removing an Element
my_set.remove(3)

# Discarding an Element
my_set.discard(4)

# Popping an Element (Random)
popped_element = my_set.pop()

# Clearing a Set
my_set.clear()

# Checking if Element is in Set
is_present = 7 in my_set

# Union of Sets
union_set = my_set.union({10, 11, 12})

# Intersection of Sets
intersection_set = my_set.intersection({2, 4, 6})

# Difference of Sets
difference_set = my_set.difference({1, 3, 5})

# Symmetric Difference of Sets
symmetric_difference_set = my_set.symmetric_difference({4, 5, 6})

# Subset Check
is_subset = {1, 2}.issubset(my_set)

# Superset Check
is_superset = my_set.issuperset({1, 2, 3})

# Checking Disjoint Sets
are_disjoint = my_set.isdisjoint({7, 8, 9})

# Copying a Set
new_set = my_set.copy()

# Frozen Set (Immutable Set)
frozen_set = frozenset(my_set)

# Length of Set
length_of_set = len(my_set)

# Element level access 
for i in my_set:
    print(i)