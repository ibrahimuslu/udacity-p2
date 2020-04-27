def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # initialize pointers for the positions of 0 and 2
    last_0_pos = 0 # first position
    first_2_pos = len(input_list) - 1 #last position

    traverse_pos = 0
    #traverse the list forward and backwards
    while traverse_pos <= first_2_pos: # not necessary to traverse until end of list
        if input_list[traverse_pos] == 0: # encountered with 0 
            input_list[traverse_pos] = input_list[last_0_pos] # then take the value of last 0 position to this known value position
            input_list[last_0_pos] = 0 # and put 0 to the last 0 position
            last_0_pos += 1 # and move forward
            traverse_pos += 1
        elif input_list[traverse_pos] == 2: # encountered with 2 
            input_list[traverse_pos] = input_list[first_2_pos] # then take the value of first 2 position to this known value position
            input_list[first_2_pos] = 2 # and put 2 to the first 2 position
            first_2_pos -= 1 # after swap move backward
        else: # encountered with 1
            traverse_pos += 1 # dont change nothing but go on traversing. Swapping handle placing 1s in correct position
    return input_list
def test_function(test_case):
    # print(test_case)
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
import random
l0 = [0 for i in range(20)]
l1 = [1 for i in range(20)]
l2 = [2 for i in range(20)]
l = []
l.extend(l0)
l.extend(l1)
l.extend(l2)
random.shuffle(l)
test_function(l)