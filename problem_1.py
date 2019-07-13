def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        number = int(number)
        if number < 0:
            return None 
        # Base cases
        if (number == 0 or number == 1) :
            return number

        # Do Binary Search for floor(sqrt(number))
        start = 1
        end = number
        while (start <= end) :
            mid = (start + end) // 2

            # If number is a perfect square
            if (mid*mid == number) :
                return mid

            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than number, and move closer to sqrt(number)
            if (mid * mid < number) :
                start = mid + 1
                ans = mid

            else :

                # If mid*mid is greater than number
                end = mid-1
        return ans
    except ValueError:
        return None

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
