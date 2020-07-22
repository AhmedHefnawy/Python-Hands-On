
""""
when you need a short throw away function
or something simple you will use it once
Anonymous Function = Lambda expression = No Name
 ^^^the General way to write your lamda exprssion
 lambda INPUTS : <Expression>
"""

def f(x):
    """" V1) by The standard Approuch """
    return 3*x + 1

print("Running function V1 : ",f(2))
# let to write the same function by lambda expression
"""" V2) by The Lambda Expression """
g = lambda x: 3*x + 1
print("Running function V2 : ",g(2))

#************** Lambda Expression with multiple inputs ****************
""" compine first name and last name onto a single FULL NAME  """
FULL_NAME = lambda first_name , last_name : first_name.strip().title() + " " + last_name.strip().title()
print("My Name is :", FULL_NAME("                   ahmed", "   Hefnawy"))

# ^^^^^^^^^^^^^^^^^^^^^^^^ Let to use Function with no name ^^^^^^^^^^^^^
"""" Sort a list using a last letter that every element has a multi character """
authors = ["aw ds fb" , "Qf Pbb Gnf" ,"Yf Uk Khjbgb" , "Luy Reg" , "bhth grerg Gfrbtr" , "fw" ,"Ge Efg Ikl"]
authors.sort(key=lambda name: name.split(" ")[-1].lower())
print("Sorted List Is:" , authors)

#^^^^^^^^^^^^^^^^^^^^^^^^^ Quadratic Function by lambda expression ^^^^^^^^^^^^^^^^^^
def build_quadratic (a , b , c) :
    """return f(x)= ax^2 + bx + c """
    return lambda x: a*x**2 + b*x + c

f = build_quadratic(3 , 0 , 1)
print("Quadratic           = " , f(2))

print("Quadratic By lmabda = " , build_quadratic(3,0,1)(2)) #>>>> 3x^2 + 1 Evaluated for x=2
# #################################### Let's play with lambda

NewQ = lambda a , b , c , x : a*x**2 + b*x + c

print("Native lamda Quadaratic :" , NewQ(3 , 0 , 1 , 2) )

""""WRITE ANY INPUTS YOU WANT TO COMPUTE AND GO TO CALL YOUR METHOD :)_* """