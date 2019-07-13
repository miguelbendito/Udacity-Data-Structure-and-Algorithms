def rotated_array_search (input_list, start, end, number):
    if start > end:
        return -1

    mid = (start + end) // 2
    if input_list[mid] == number:
        return mid

    # If arr[l...mid] is sorted
    if input_list[start] <= input_list[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if number >= input_list[start] and number <= input_list[mid]:
            return rotated_array_search(input_list, start, mid-1, number)
        return rotated_array_search(input_list, mid+1, end, number)

    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if number >= input_list[mid] and number <= input_list[end]:
        return rotated_array_search(input_list, mid+1, end, number)
    return rotated_array_search(input_list, start, mid-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list,0, len(input_list)-1, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
