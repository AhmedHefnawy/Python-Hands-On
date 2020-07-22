import time
import math
""" VERSION TWO >> WE WILL TEST ALL Integrs and check the prime number in ALL """
def Is_Prime_V1 (n) :     # Version one
    """return true if integer is prime and false if not"""
    if n == 1 : # number one is a unit not prime or composite
        return False

    for d in range(2 , n) :
        if n % d == 0 :
            return False
    return True
# =============== Test Complexity Function ===========
t_start = time.time()
for n in range (1 , 15551):
    Is_Prime_V1(n)
t_end = time.time()
print("Time required in V1 =" , t_end - t_start)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^************* End of Version One *******^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""" VERSION TWO >> WE WILL TEST ALL DIVISORS FROM 2 THROUGH sqrt(n) <<< Math trick """
def Is_Prime_V2(x) :
    """return true if integer is prime and false if not"""
    if x == 1 :
        return False

    max_divisor = math.floor(math.sqrt(x))
    for k in range(2, 1 + max_divisor):
        if x % k == 0:
            return False
    return True

# =============== Test Complexity Function ===========
t_start = time.time()
for x in range (1 , 15551):
    Is_Prime_V2(x)
t_end = time.time()
print("Time required in V2 =" , t_end - t_start)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^************* End of Version Two *******^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""" VERSION THREE >> WE WILL USE 2 STEPS TO IMPROVE OUR FUNCTION 
STEP 1) > Test if n is EVEN or not
STEP 2 ) test only Odd Divisors                                  """

def Is_Prime_V3(f) :
    """return true if integer is prime and false if not"""
    if f == 1 :
        return False
    #if number is even and not 2 ,, then it's Not Primne
    if f == 2 :
        return True
    if f > 2 and f % 2 == 0 :
        return False

    max_divisor = math.floor(math.sqrt(f))
    for k in range(3, 1 + max_divisor , 2):  # we will add three parameter >> This range will start from three and will cover all even number up to the limit ,, 2 is Counter
        if f % k == 0:
            return False
    return True

# =============== Test Complexity Function ===========
t_start = time.time()
for x in range(1, 15551):
    Is_Prime_V3(x)
t_end = time.time()
print("Time required in V3 =", t_end - t_start)



""""
Time required in V1 = 1.2563598155975342
Time required in V2 = 0.031247377395629883
Time required in V3 = 0.01565694808959961  
"""














