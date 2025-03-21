# ARITHMETIC OPERATOR;;
print(5+6)
print(7-5)
print(5*6)
print(12/4)
print(5//2)    #floor division
print(5%2)       #modulus
print(5**2)      #repetition

# RELATIONAL OPERATOR;;
print(4>5)     #greater than
print(4<5)     #less than
print(4>=5)    #greater than or equal to
print(4<=5)    #less than or equal to
print(4==4)    #equal to
print(4!=4)    #not equal to

# LOGICAL OPERATOR;;
print(1 and 0)
print(1 or 0)
print(not 1)

# BITWISE OPERATOR;;
print(2 & 3)    #bitwise and
print(2 | 3)    #bitwise or 
print(2 ^ 3)    #bitwise xor
print(~3)
print(4>>2)     #bitwise left operator
print(5<<2)     #bitwise left

# ASSIGNMENT OPERATOR;;
a=2
a+=2
print(a)

# MEMBERSHIP OPERATOR;;
print("d" in 'delhi')
print("k" in 'delhi')
print("u" not in "khushbu")
print(1 in [1,2,3,4,5,6])

# Q-WAP TO FIND THE SUM OF A 3 DIGIT ENTERED BY THE USER?
num=int(input("Enter a 3 digit number : "))
a=num%10        #like 345%10->5
b=num%10        #like 34%10->4
num=num//10
c=num%10       #like 3%10->3
print(a+b+c)

# IF ELSE IN PYTHON;;WAP TO CHECK CONDTIONS EMAIL AND PASSWORD?
email=input("Enter email : ")
password=input("Enter password : ") 
if(email=='khushbu.python@gmail.com' and password=="1234"):
    print("Password and Email is valid!!")
else:
    print("Not valid!!")

# TO CHECK MORE POSSIBILITIES;;
email=input("Enter Email : ")
password=input("Enter Password : ")
if(email=="khushbu.python@gmail.com" and password=='1234'):
    print("Password and Email is valid!!")

elif(email=='khushbu.python@gmail.com' and password!='1234'):
    print("Incorrect password")
    password=input("Enter password again = ")
    if(password=="1234"):   #NESTED IF ELSE STATEMENT 
        print("Welcome finally !")
    else:
        print("U cannot do it !")

else:
    print("Not valid !!")

# WAP TO CHECK MINIMUM NUMBERS?
a=int(input("Enter first num :"))
b=int(input("Enter second num :"))
c=int(input("Enter third num :"))

if(a<b and a<c):
    print("a is smallest : ",a)
elif(b<c):
    print("b is smallest : ",b)
else:
    print("C is smallest : ",c)

# MENU DRIVEN CALCULATOR;;
num1=int(input("Enter a first number  : "))
num2=int(input("Enter a second number  : "))
result=input("Enter the operation : ")
if(result=="+"):
    print(num1+num2)
elif(result=="-"):
    print(num1-num2)
elif(result=='*'):
    print(num1*num2)
else:
    print(num1/num2)

# MODULES;;MATH
import math
print(math.factorial(5))
print(math.floor(6.7))
print(math.sqrt(4))

# KEYWORDS;;
import keyword
print(keyword.kwlist)

# RANDOM MODULE
import random
print(random.randint(1,100))

# DATETIME MODULE;;
import datetime
print(datetime.datetime.now())

print(help('modules'))   #to check the modules

# LOOPS IN PYTHON;;FOR AND WHILE;;WAP TO PRINT THE TABLE?
num=int(input("Enter a number : "))
i=1
while(i<11):
    print(num,'*',i,'=',num*i)
    i+=1

# WHILE LOOP WITH ELSE:
x=1
while(x<3):
    print(x)
    x+=1
else:
    print("Limit crossed")

# GUESSING GAME;;
import random
jackpot=random.randint(1,100)
guess=int(input("Guess number : "))
counter=1

while(guess!=jackpot):
    if(guess<jackpot):
      print("Wrong! Guess higher")
    else:
      print('Wrong! Guess lower')
    
    guess=int(input("Guess number again ="))
    counter+=1
else:
   print("Correct guess")
   print("Attempts",counter)

# FOR LOOP DEMO;;
for i in range(1,20,2):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in 'delhi':
    print(i)
for i in [1,2,3,4,5]:
    print(i)

# WAP TO THE CURRENT POPULATION OF TOWN IS 10000 THE POPULATION OF THE TOWN IS INCREASING AT THE RATE OF 10%PER YEAR.YOU HAVE TO WRITE A PROGRAM TO FIND OUT THE POPULATION AT THE END OF EACH OF THE LAST 10 YEARS?
curr_population=10000
for i in range(10,0,-1):
    print(i,curr_population)
    curr_population=curr_population/1.1