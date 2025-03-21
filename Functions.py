# LETS CREATE A FUNCTION OF ODD AND EVEN?
def is_even(num):
    """
    this function returns if a given number is odd or even 
    input-any valid integer
    output-odd/even
    created on - 15th March,2025
    """
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

for i in range(1,11):
    x=is_even(i)
    print(x)
print(is_even.__doc__)

# DEFAULT ARGUMENTS;;
def power(a=1,b=1):
    return a**b
print(power(2,3))
print(power())
print(power(4))

# POSITIONAL ARGUMENTS;;
def power(a=1,b=1):
    return a**b
print(power(2,3))   #if we send something arguments then paramater will handle on positionly.
print(power())
print(power(4))

# KEYWORD ARGUMENTS;;;
def power(a=1,b=1):
    return a**b
print(power(2,3))
print(power())
print(power(4))
print(power(b=3,a=2))    #keyword arguments

# ARGS**
def multiply(*args):
    product=1
    for i in args:
        product=product*i
    return product

print(multiply(1,2,3,4,5,6,7,8,9,10))

# KWARGS**
def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key," = ",value)
print(display(India="Delhi",Mumbai="Pune",Uttarpradesh="lucknow",pakistan="Islamabad"))

# GLOBAL VARIABLE vs LOCAL;;
def g(y):   # 'y' is a local variable (parameter)
    print(x)   # Using global 'x'
    print(x + 1)  # Using global 'x'

x = 5  # Global variable
g(x)  # Calling function g with X
print(x)  # Printing global x

def f(y):  
    x = 1  # Local variable 
    x += 1  
    print(x)  

x = 5  # Global variable 'x'
f(x)  # Calling function 'f' 
print(x)  

def h(y):
    global x  # Declares that we're using the global 'x'
    x += 1  # Modifies the global 'x'

x = 5  # Global variable
h(x)  # Function call
print(x)  # Print the modified global x

def f(x):
    x=x+1
    print("In f(x): x = ",x)
    return x
x=3
z=f(x)
print("In main program scope : z = ",z)
print("In main program scope : x = ",x)

# NESTED FUNCTIONS;;
def f():
    def g():
        print("Inside function g")
    g()
    print("Inside function f")
f()

def g(x):
    def h():
        x="abc"
    x=x+1
    print("In g(x): x = ",x)
    h()
    return x
x=3
z=g(x)

def g(x):
    def h(x):
        x=x+1
        print("In h(x) : x = ",x)
    x=x+1
    print("In g(x): x = ",x)
    h(x)
    return x

x=3
z=g(x)
print("In main program scope : x = ",x)
print("In main program scope : z = ",z)

# FUNCTION ARE 1ST CLASS CITIZEN;;
def square(num):
    return num**2
print(type(square))          #type and id
a=2
print(type(a))
print(id(square))
x=square
print(id(x))
print(x(3))          #reassign
del square    #delete
print(square(3))
l=[1,2,3,4,square]     #storing a values
print(l[1])

# RETURNING A FUNCTION;;
def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)

# FUNCTION AS ARGUMENT;;
def func_a():
    print("Inside func_a")
def func_b(z):
    print("Inside func_b")
    return z
print(func_b(func_a))

# LAMBDA FUNCTION;;
s=lambda x:x**2    #square
print(s(12))

a=lambda x,y:x+y    #add
print(a(5,2))

# CHECK IF A STRING HAS "A" BY LAMBDA?
a=lambda s: "a" in s
print(a("hello"))
print(a("Khushbu saifi"))

# # CHECK NUMBER IS ODD OR EVEN?
s=lambda x: "even" if x%2==0 else "odd"
print(s(6))
print(s(3))

# HIGHER ORDER FUNCTIONS;;
def square(x):
    return x**2

def cube(x):
    return x**3

def transform(f,l):
    output=[]
    for i in l:
        output.append(f(i))
    print(output)

l=[1,2,3,4,5]
print(transform(lambda x:x**2,l))
print(transform(lambda x:x**3,l))

# WAP TO PRINT SQUARE THE ITEMS OF A LIST USING MAP FUNCTION?
print(list(map(lambda x:x**2 ,[1,2,3,4,5,6,7,8,9])))

# WAP TO PRINT LABELLING OF LIST ITEMS;;
l=[1,2,3,4,5,6]
print(list(map(lambda x:"Even" if x%2==0 else "odd" ,l)))

# WAP TO PRINT EXTRACT NAMES IN A DICT?
users=[
    {
        "Name":"Rahul",
        "Age":34,
        "Gender":"Male"
    },

    {
        "Name":"Mohit",
        "Age":23,
        "Gender":"Male"
    },
  
    {   "Name":"Riya",
        "Age":20,
        "Gender":"Female"
    }
]

print(list(map(lambda users:users["Gender"],users)))
print(list(map(lambda users:users["Age"],users)))
print(list(map(lambda users:users["Name"],users)))

# WAP TO PRINT NUMBERS GREATER THAN 5 BY USING FILTER FUNCTION?
l=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x>5,l)))

# WAP TO PRINT FETCH FRUITS STARTING WITH "a"?
fruits=["apple","guava","banana"]
print(list(filter(lambda x:x.startswith('a'),fruits)))

# WAP TO PRINT SUM OF ALL ITEMS BY USING REDUCE FUNCTION?
import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6]))

# # WAP TO PRINT MIN NUMBER?
import functools
print(functools.reduce(lambda x,y:x if x<y else y,[1,2,3,4,5,6,77]))