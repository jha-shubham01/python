# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtube.com/shorts/QdEd5r0XqzQ


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print(f"Decorator Before!! {args}")
        func(*args, **kwargs)
        print(f"Decorator After!! {args}")

    return wrapper


@decorator_func
def greet(name):
    print(f"Greet!! Welcome, {name}!")

greet("John")
