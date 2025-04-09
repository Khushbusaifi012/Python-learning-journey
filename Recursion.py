def multiply(a,b):   
    result=0
    for i in range(b):
       result=result+a
    print(result)    
multiply(3,4)

# PRODUCT FUNCTION THROUGH RECURSION;;
def mul(a,b):
    if b==1:
        return a
    else:
        return a+mul(a,b-1)
print(mul(4,5))

# FACTORIAL FUNCTION THROUGH RECURSION;;
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

# PALINDROME NUMBERS THROUGH RECURSION;;
def palin(text):
    if len(text)<=1:
        print('Palindrome numbers')
    else:
        if text[0]==text[-1]:
            palin(text[1:-1])
        else:
            print('Not a palindorme')
palin('Madam')
palin('Malayalam')
palin('Python')
palin('madam')

# FIBONACCI SERIES THROUGH RECURSION;;
def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
print(fib(5))