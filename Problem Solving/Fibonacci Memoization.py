import timeit
fibonacci_Cache ={}
def fibonacci(n):
    #if value cached , return it
    if n in fibonacci_Cache:
        return fibonacci_Cache[n]

    #compute function!!
    if n == 1 :
        value = 1
    elif n == 2 :
        value = 1
    elif n > 2 :
        value = fibonacci(n-1) + fibonacci(n-2)

    #cach the value and return it !!1
    fibonacci_Cache[n] = value
    return value

for n in range(1,1001) :
    print (n, ":" , fibonacci(n))
