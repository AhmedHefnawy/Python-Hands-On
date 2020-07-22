
def fibonacci(n):
    #compute function!!
    if n == 1 :
        return  1
    elif n == 2 :
        return  1
    elif n > 2 :
        return  fibonacci(n-1) + fibonacci(n-2)

for n in range(1,1001) :
    print (n, ":" , fibonacci(n))
