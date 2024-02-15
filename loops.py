# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/3aE7hDzkgQs


# # For Loop
# # Sequence can be list, tuple, set, dictionary, and string

# sequence = ["apple", "banana", "orange"]
# for fruit in sequence:
#     # Code to be executed for each item
#     print(f"I love eating {fruit}!")


# # While Loop
# guess_count = 0
# while guess_count < 3:
#     guess = input("What is your guess? ")
#     guess_count += 1

#     if guess == "secret":
#         print("Congratulations! You guessed the secret!")
#         break

# if guess_count == 3:
#     print("Sorry, you ran out of guesses.")


# # For Else
# sequence = ["apple", "banana", "orange"]
# for fruit in sequence:
#     # Code to be executed for each item
#     print(f"I love eating {fruit}!")
#   if fruit == "apple":
#       break
# else:
#     # Code to be executed if the loop finishes normally
#     print("Else code block executed")


# # Nested Loops
# sequence = [["apple","banana", "orange"], ["Broccoli", "Garlic"]]
# for items in sequence:
#     print("Printing new items:")
#     for item in items:
#         print(f"Item is {item}!")

# Comprehension For loop
sequence = ["apple","banana", "orange"]
# [print(fruit) for fruit in sequence]

[print(fruit) for fruit in sequence if fruit.startswith("a")]

[
    print(fruit) 
    if fruit.startswith("a") 
    else print(f'I don\'t like {fruit}!') 
    for fruit in sequence
]

