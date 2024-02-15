# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtu.be/KClYO794q-Q


def greet_user(name):
    print(f"Hello {name}!")


name = input("What is your name? ")
greet_user(name)



def area(length, width):
    area = length * width
    return area

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print(f"Area is: {area(length, width)}")