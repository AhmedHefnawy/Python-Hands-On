import math

""""
Data (d) : list or tuple or sets or any data collection store
Function(f) : function
------------------ and you want to perform the function (f) in all element of data (d)
map( function , data ):
Return iterator over
all fuinction(element)
"""
# Data .......

# Function ``````
def area(r) :
    """" calculate the area of circit = pi * r^2 """
    return math.pi * (r**2)

radii = [3 , 5 , 7.1 , 0.3 , 10 ]
# The direct method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print("AREAS        : " , areas)

print("AREAS BY MAP : ",list(map(area, radii))) # TO PRINT your map objevt you have to put in list object

# IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
"""" Convert you c to f >>> F = 9/5 * c + 32"""
tmps = [("Berline", 29) , ("Cairo" , 36) , ("Los Anglos" , 26) , ("Tokyo" , 27)]
c_to_f = lambda data : (data[0], "by C >" , data[1] ,"by F", (9/5)*data[1] + 32 ) #data[0] >> 0 is the (0,1,2,...,n) of tmps elemnts to print
print("The New F List :",list(map(c_to_f , tmps)))