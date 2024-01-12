
# For Loop
# Sequence can be list, tuple, set, dictionary, and string

sequence = ["apple", "banana", "orange"]
for fruit in sequence:
    # Code to be executed for each item
    print(f"I love eating {fruit}!")


# While Loop
guess_count = 0
while guess_count < 3:
    guess = input("What is your guess? ")
    guess_count += 1

    if guess == "secret":
        print("Congratulations! You guessed the secret!")
        break

if guess_count == 3:
    print("Sorry, you ran out of guesses.")


# For Else
sequence = ["apple", "banana", "orange"]
for fruit in sequence:
    # Code to be executed for each item
    print(f"I love eating {fruit}!")
else:
    # Code to be executed if the loop finishes normally
    print("Else code block executed")