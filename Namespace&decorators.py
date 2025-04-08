# LOCAL AND GLOBAL SCOPE;;
a=2   #global variable
def temp():
    b=3   #local variable
    print(b)
temp()
print(a)

# GLOBAL AND LOCAL WITH SAME VARIABLE;;
a=2  
def temp():
    a=3
    print(a)
temp()
print(a)

# LOCAL AND GLOBAL ->LOCAL DOES NOT HAVE BUT GLOBAL HAS;;
a=2
def temp():
    print(a)
temp()
print(a)

# LOCAL AND GLOBAL->EDITING GLOBAL;;
# a=2
# def temp():
#     a+=1
#     print(a)
# temp()
# print(a)   #it will give us error because we cannot do changes

a=2
def temp():
    global a    #but we have a global variable to modify it
    a+=1
    print(a)
temp()
print(a)

# LOCAN AND GLOBAL ->GLOBAL CREATED INSIDE LOCAL;;
def temp():
    global a 
    a=1
    print(a)
temp()
print(a)

# LOCAL AND GLOBAL->GLOBAL CREATED INSIDE LOCAL;;
def temp(z):
    print(z)
a=5
temp(5)
print(a)

# BUILT-IN-SCOPE;;
import builtins
print(dir(builtins))

# REMAINING BUILT-INS;;
# l=[1,2,3,4]
# max(l)
# def max():
#     print('hello')
# max(l)

# ENCLOSING SCOPE;;
def outer():
    def inner():
        print('inner function')
    inner()
    print('outer function')
outer()
print('main program')

# PYTHON ARE FIRST CLASS FUNCTION;;
def func():
    print('hello')
a=func
a()
# del func   #to delete function
# func()

def modify(func,num):
    return func(num)    #decorator
def square(num):  
    return num**2    #input
print(modify(square,2))

# SIMPLE EXAMPLE IN DECORATOR;;
def my_decorator(func):
    def wrapper():
        print('*****************')
        func()
        print('*****************')
    return wrapper

@my_decorator
def hello():
    print('hello')

def display():
    print('Hello python')
a=my_decorator(hello)
a()
b=my_decorator(display)
b()

# MEANINGFULL DECORATOR;;
import time
def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken by :',func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def hello():   #first function with decorator
    print('hello world')
    time.sleep(2)

@timer
def display():   #second function with decorator
    print('displaying something')
    time.sleep(4)

@timer    #third function with decorator
def square(num):
    time.sleep(1)
    print(num**2)
   
@timer 
def power(a,b):   #fourth function with decorator
    print(a**b)

hello()
display()
square(2)
power(2,3)

# A BIG PROBLEM;;
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args)==data_type:
                func(*args)
            else:
                raise TypeError('This is not datatype')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

@sanity_check(str)
def greet(name):
    print('hello',name)

square(2)
# square('python')  # this will raise error
greet('Khushbu')
# greet(5)   # this will raise error