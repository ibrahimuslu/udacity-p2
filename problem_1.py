def sqrt(number):
    """
        Calculate the floored square root of a number

        Args:
        number(int): Number to find the floored squared root
        Returns:
        int: Floored Square Root
    """
    def sqrt_search(the_array, item, start, end):
        if start == end:
            return start
        if start > end:
            return start-1
        mid = (start + end)// 2
        # print(start,mid, end)

        # print(the_array[start],the_array[mid], the_array[end])
        if mid**2 < item:
            return sqrt_search(the_array, item, mid + 1, end)

        elif mid**2 > item:
            return sqrt_search(number, item, start, mid - 1)

        else:
            return mid

    return( sqrt_search(number, number, 0,number))
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(35)) else "Fail")
print ("Pass" if  (25 == sqrt(625)) else "Fail")
print ("Pass" if  (25 == sqrt(628)) else "Fail")
print ("Pass" if  (100000 == sqrt(10000000000)) else "Fail")
print ("Pass" if  (0 != sqrt(-1)) else "Fail")