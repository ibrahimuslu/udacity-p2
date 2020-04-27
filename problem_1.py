def sqrt(number):
    """
        Calculate the floored square root of a number

        Args:
        number(int): Number to find the floored squared root
        Returns:
        int: Floored Square Root
    """

    for i in range(number+1):
        if(i*i) == number:
            return i
        if(i*i) > number:
            return (i-1)
    return 0
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (25 == sqrt(625)) else "Fail")
print ("Pass" if  (100000 == sqrt(10000000000)) else "Fail")
print ("Pass" if  (0 == sqrt(-1)) else "Fail")