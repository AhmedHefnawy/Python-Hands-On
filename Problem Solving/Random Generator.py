import random
#print (dir(random))

#Print a  rundom number in INTERVAL [x,y) foe ex ::3,7
# 1- call random () :  #in [0,1)
# 2- scall Number ( multiply by 4 )
# 3- shift number ( add 3 )
# :(
from pip._vendor.urllib3.contrib.pyopenssl import orig_util_SSLContext

print("BY CRACH Way")
for i in range(10) :
    print(4*random.random()+3)


#YOU CAN USE UNOFIORM FUNCTION TO THIS IN SIMPE WAY :))))
print("BY USING UNIFORM FUNCTION !!!!")
for x in range(10) :
        print(random.uniform(3,7))
# to Generate a randome number from a NOrmal Distribution mu and segma >> BILL GARAgh
#use normalvariates method
print("GENERATE NUMBERAS FROM NORMAL DIS INTERVAL")
for b in range(5) :
    print(random.normalvariate(5 , 0.2))


#TO GEETRATE A RANDOM INTEGERS USE >>>> ranit(min, max)
print("GEETRATE A RANDOM INTEGERS")
for t in range(20):
    print(random.randint(1,6)) #take an integer Arguments

#TO GEETRATE A RANDOM element from list USE choice(outcomes) method
print("^^^^^^^random choice paly^^^^^^^^^^^^")
otcomes = ['rock','paper','scissors']

for k in range(4):
    print(random.choice(otcomes))
