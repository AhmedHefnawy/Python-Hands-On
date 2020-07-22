import time
from functools import reduce

""""
Dta (d) : collection data
function (F) : f(x,y)

reduce (f , data )
>
step 1 : Val 1 = F(a1 , a2 )
step 2 : Val 2 = F(Val1 , a3)
step 3 : Val 3 = F(Val2 , a4)
.
.
.
.
step n-1 : Val n-1 = F(Val(n-2) , a(n) )
Return Val (n-1)
----------
Alternatively :
Returns f (f (f (f (a1,a2 ) , . . ..a(n) )
"""

# >>>>>>>>>> Multiply all numbers in a list

# Data collection d
data = [2,6,4,8,7,6,2,6,2,4,9,6,32,2,6,3,98,22,652,55,4,484847,48]
tt = time.time()
# function f
multiplyer_function = lambda x , y : x*y

# Perform reduce function

print("Using Reduce fucnction ::" ,reduce(multiplyer_function , data) )
ttt = time.time()
print("the time of resuce is :" , ttt - tt)

answer = 1
to = time.time()
for l in data :
    answer = answer * l

print("Using For loop ::" , answer)
tz = time.time()
print("the time of for loop is :" , tz - to)