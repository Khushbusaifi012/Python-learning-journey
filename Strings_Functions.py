# SEQUENCE SUM;;
# n=int(input("Enter n : "))
# result=0
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     result=result+i/fact
# print(result)

# NESTED LOOPS;;
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# ASTERISK PATTERN;;;
# rows=int(input("Enter rows : "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#        print('*',end=" ")
#     print()

# row=int(input("Enter rows : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()

# LOOP CONTROL STATEMENTS;;BREAK,CONTINUE AND PASS;
# for i in range(1,10):  #BREAK STATEMENT
#     if(i==5):
#         break
#     print(i)

# CHECK PRIME NUMBERS?
# lower=int(input("Enter lower range : "))
# upper=int(input("Enter upper range : "))
# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if(i%j==0):
#            break
#     else:
#         print(i)

# CONTINUE STATEMENT;;
# for i in range(1,10):
#     if(i==5):
#         continue
#     print(i)

# PASS STATEMENT;;
# for i in range(1,10):
#     pass

# HOW TO CREATE A STRINGS?
# s='hello'
# s="hello"
# s='''hello'''    #for multiline strings
# s="""hello"""
# s=str('hello')
# print(s)

# HOW TO ACCESS SUBSTRINGS FROM A STRING? INDEXING
# s="hello world"
# print(s[0])
# print(s[-1])

# s="hello world"
# print(s[0:3])     #slicing
# print(s[2:3])
# print(s[::-1])
# print(s[0:6:2])
# print(s[-5:])
# print(s[-1:-6:-1])

# EDITING AND DELETING A STRING?
# s="hello world"
# s[0]="H"
# print(s)   #python strings are immutable

# s="hello world"
# del s
# print(s)

# s="hello world"
# del s[-1:-5:2]
# print(s)    #not to worked

# OPERATION ON STRINGS;;  ARITHMETIC
# print('delhi'+'mumbai')    #concatenation
# print('delhi'*5)           #repetition
# print("*"*50)

# RELATIONAL;;
# print('delhi'=='delhi')
# print('delhi'!='delhi')
# print('delhi'=='mumbai')
# print('mumbai'>'pune')
# print('delhi'=="Delhi")

# LOGICAL;;
# print('hello' and 'world')
# print('hello' or 'world')
# print(not  'world')

# LOOPS;;
# for i in ('hello'):
#     print(i)

# for i in('delhi'):
#     print('pune')

# # MEMBERSHIP;;
# print('d' in 'delhi')
# print('k' not in 'delhi')

# COMMON FUNCTIONS(LEN,MAX,MIN,SORTED):
# print(len('helllo wolrd'))
# print(max("hello world"))
# print(min("hello world"))
# print(sorted("hello world"))
# print(sorted("hello world",reverse=True))

# CAPITALIZE,TITLE,UPPER,LOWER,SWAPCASE;;
# s="hello world"
# print(s.capitalize())   
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())

# COUNT,FIND,INDEX;;
# print("khushbu is a girl".count("i"))
# print("khushbu is a girl".find("i"))
# print("khushbu is a girl".find("x"))
# print("khushbu is a girl".index("a"))
# print("khushbu is a girl".index("x"))

# ENDWITH AND STARTSWITH;;
# print("khushbu is a girl".endswith("a"))
# print("khushbu is a girl".endswith("rl"))
# print("khushbu is a girl".startswith("a"))
# print("khushbu is a girl".startswith("k"))

# FORMAT;;
# name="khushbu"
# gender='female'
# print('Hi my name is {} and I am a {}'.format(name,gender))

# ISALNUM,ISALPHA,ISDIGIT,ISIDENTIFIER;;
# s="khushbu12344"
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isidentifier())

# SPLIT,JOIN,REPLACE,STRIP;;
# s='khushbu is a girl'
# print(s.split())
# s="delhi is a city"
# print(" , ".join(s))
# print("-".join(s.split()))
# s="khushbu is a girl"
# print(s.replace('khushbu','campusx'))
# s='beautiful rain'
# print(s.                       strip())