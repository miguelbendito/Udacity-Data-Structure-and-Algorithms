def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = 0
    min = 0
    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, len(ints)):
        if ints[i] > max:
            max = ints[i]
        if min > ints[i]:
            min = ints[i]
    return min,max
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
min, max = get_min_max(l)
# print("max int: " + str(max) + ", min int: " + str(min))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 6)]  # a list containing 0 - 5
random.shuffle(l)
print ("Pass" if ((0, 5) == get_min_max(l)) else "Fail")
