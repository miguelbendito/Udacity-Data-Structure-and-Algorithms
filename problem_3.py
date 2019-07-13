def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = countSort(input_list)

    number_1 = 0
    number_2 = 0
    for count, i in enumerate(sorted_input_list):
        # print("count var: " + str(count) + " i var: " + str(i))
        if count % 2 == 0:
            number_2 = number_2 * 10 + i
            # print("max sum 2: " + str(number_2))
        else:
            # print("max sum 1:" + str(number_1))
            number_1 = number_1 * 10 + i

    maximum_sums = [number_1, number_2]

    return maximum_sums

    pass

# The main function that sort the given string arr[] in
# alphabetical order
def countSort(arr):

    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]]
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    count_desc = len(arr) -1
    for i in range(len(arr)):
        ans[i] = output[count_desc]
        count_desc -=1
    # print(ans)
    return ans

# Driver program to test above function

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[0,0], [0, 0]])
