#>>> With list comprehensions you can create or sperate a list with any condition >> in one single line
#general formatat [ expression (to generate the elements in list)            for  val  in  collection                 ]
#                               1>>                                          2 >> over for loop with some condition in data collection !!

#First examble >> generate a square list in range
# version one in general way

square = []  # 1) create your empty list
for i in range(1,101) :
    square.append(i**2)
print ("Genneral WaY",square)

# version 2 in list comprehensions way
square_Com =  [ l**2 for l in range(1,101) ] # in only one single line you can do it !!!!!!!!!!!!!!
print("Comprehensions WaY",square_Com)



remainder5 =  [ x**2 % 5 for x in range(1,101) ] # And so ON :)
print("Comprehensions WaY",remainder5)


print(">>>>>>>>>>>>>>>>>>>>     let's Using if condition     <<<<<<<<<<<<<<<<<<<<")

movies = ["Aman" , "Boz" , "Zara" , "Adidase" , "Toshipa" , "Gold" , "GDG" , "Code" , "Microsoft" , "Adobe" , "Gad" , "Gehad"]
# i want to generate a new list from this list by an if condidtion or filter
# version one by normal way
A_movies = []
for s in movies :
    if s.startswith("A"):
        A_movies.append(s)
print("A : = " , A_movies)

# version two by comprehensions way
G_movies = [s for s in movies if s.startswith("G")] #<< in only one single line you can do it
print("G : = " , G_movies)

print("<<<<<<<<<<<<  let's to Work on Tuples :) >>>>>>>>>>>>>>>>>>>>>")
v = [3 , 6 , 8]
print("It's Not we Want",4*v) # it will duplicate list 4 times , but we need to multipling it

w = [4*i for i in v]
print("Thats we rally want " , w)


print("<<<<<<<<<<<<<<<<<<  SOLVE CARTESIAN PRPODUCT PROBLEM IN TWO or more SETS>>>>>>>>>>>>>>>>>>>>")
A = [1,2,3,4]
B = ["a","b","c","d"]
C = ['/' , '*','-','+']
A_U_B_U_C = [(a,b,c) for a in A for b in B for c in C]
print("The Union CArtisian Product = " , A_U_B_U_C)























