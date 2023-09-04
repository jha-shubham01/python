# By Shubham Jha
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: 


"""Python way to get values lists in sorted order"""


def get_values(data):
    return sorted(data.values())


if __name__ == '__main__':
    case1 = get_values({'a':987, 'b': 121, 'c':654})
    print(case1)
    assert case1 == [121, 654, 987]
    
    case2 = get_values({'a': 3, 'b': 25, 'c': 98, 'd': 0, 'e': -5, 'f': 0})
    print(case2)
    assert case2 == [-5, 0, 0, 3, 25, 98]
    
    print('Success')
