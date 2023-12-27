# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: https://youtube.com/shorts/dGr8y3WTmwQ?feature=share

print("1. Check Even numbers")
# 1. Check Even numbers
def even_numbers():
    num = 0
    while True:
        if num % 2 == 0:
            yield num
        num += 1


even_nums = even_numbers()


even_number_list = [next(even_nums) for _ in range(10)]
print(even_number_list)


print("2. Generate fibonacci series")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibo = fibonacci()

fibonacci_list = [next(fibo) for _ in range(10)]
print(fibonacci_list)
