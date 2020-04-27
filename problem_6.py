
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_index = 0
    min_index = len(ints) - 1
    front = 0
    for (index, value) in enumerate(ints):
        if value > ints[max_index]:
            max_index = index
        if value < ints[min_index]:
            min_index = index
    return ints[min_index], ints[max_index]

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?