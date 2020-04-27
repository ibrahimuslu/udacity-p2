import math
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def findPivot(input_list, number):
        for idx,i in enumerate(input_list):
            if i< input_list[idx-1]:
                return idx, None
            if number == i: # faster finding 
                return idx, idx
    pivot,found = findPivot(input_list, number)
    if found:
        return found
    size = len(input_list)
    def findNumber(input_list, number, pivot,start, end):
        print(input_list, number, pivot,start, end)
        if number == input_list[pivot]:
            return pivot
        elif number >= input_list[pivot] and number <= input_list[end]:
            return findNumber(input_list, number, math.ceil((end-pivot)/2)+pivot, pivot,end)
        elif number >= input_list[0] and number <= input_list[pivot-1]:
            return findNumber(input_list, number,  math.ceil((pivot-start)/2), 0,pivot-1)
        else:
            return -1
    return findNumber(input_list, number, pivot, 0, size-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    a=linear_search(input_list, number)
    b=rotated_array_search(input_list, number)
    print(a, b)
    if (a == b):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])