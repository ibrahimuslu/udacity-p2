def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    # print('left',left,'right',right)
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
    
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = mergesort(input_list)

    # print(sorted_input_list)
    first = ''
    second = ''
    for (index,i) in enumerate(sorted_input_list):
        if index % 2 == 0:
            first = str(i)+first
        else:
            second = str(i)+second

        # print(first,second)
    return int(first),int(second)
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    # print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_cases= []
test_cases.append([[1, 2, 3, 4, 5], [542, 31]])
test_cases.append([[4, 6, 2, 5, 9, 8], [964, 852]])
test_cases.append([[9, 3, 5, 2, 4, 1, 6, 0, 7, 8], [86420, 97531]])
for test_case in test_cases:
    test_function(test_case)
