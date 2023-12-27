# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/P5Bt1phtMNo

# !Note:
# Dictionary stores unique data (Duplicate will be removed)
# Dictionary doesn't have order

person = {
    "name": "Shubham",
    "age": 27,
    "hobbies": ["coding", "content creation"],
}



# Accessing Values by Key
value_of_key = person['hobbies']

# Adding a New Key-Value Pair
person['channel_name'] = 'Code with SJ'

# Updating Values
person['name'] = 'Shubham Jha'

# Removing a Key-Value Pair
del person['channel_name']

# Popping a Key-Value Pair
popped_item = person.pop('hobbies')

# Clearing the Dictionary
person.clear()

# Checking if Key is in Dictionary
is_present = 'name' in person

# Getting Value with Default
value = person.get('name', 'Shubham')

# Getting Keys
keys = person.keys()

# Getting Values
values = person.values()

# Getting Items (Key-Value Pairs)
items = person.items()

# Element level access
for key, value in person.items():
    print(key, "---->", value)

# Copying a Dictionary
new_dict = person.copy()

# Nested Dictionaries
nested_dict = {'name': {'first_name': 'Shubham', 'last_name': 'Jha'}}

# Dictionary Comprehension
squared_values = {key: value**2 for key, value in person.items()}

# Merging Dictionaries (Python 3.9 and later)
merged_dict = {**dict1, **dict2}

# Length of Dictionary
length_of_dict = len(person)

# Checking Equality
is_equal = {'a': 1, 'b': 2} == {'b': 2, 'a': 1}