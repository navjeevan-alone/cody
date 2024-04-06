from functools import cache 
global i
i=1
@cache
def factorial(n):
    global i
    print(i)
    i+=1
    return n * factorial(n-1) if n else 1

num= int(input("Enter number :"))
fact= factorial(num)
print(fact)