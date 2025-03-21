# LISTS;;
# a=2
# print(id(2))

# l=[1,2,3]
# print(id(l))
# print(id(l[0]))
# print(id(l[1]))
# print(id(l[2]))
# print(id(1))
# print(id(2))
# print(id(3))

# LISTS ORDERED;;
# L=[1,2,3]
# L1=[3,2,1]
# print(L==L1)

# CREATING A LIST;;
# print([])    #empty list
# print([1,2,3,4,5])    #1D
# print([1,2,3],[4,5])    #2D
# print([[[1,2],[3,4]],[[5,6],[7,8]]])    #3D
# print([1,10.5,True,"khushbu"])    #heterogeneous
# print(list("hello"))   #list conversion into type

# CAN CONTAIN ANY KIND OF OBJECTS;;
# l=[1,2,print,type,input]
# print(l)

# ACCESSING ITEMS FROM A LIST;;
# l=[1,2,3,[4,5]]
# print(l[0])    #indexing
# print(l[-1])
# print(l[-1][-2])
# print(l[0:3])
# print(l[-3:-1])

# ADDING ITEMS FROM THE LIST;;
# l=[1,2,3]
# l.append(100)    #append
# l.append([4,5,6])
# print(l)

# l=[1,2,3]
# l.extend([6,7,8])   #extend
# print(l)

# l=[1,2,3,4,5]
# l.extend('Khushbu')
# print(l)

# l=[1,2,3,4,5]
# l.insert(1,100)    #insert
# print(l) 

# EDITING ITEMS IN A LIST;;
# l=[1,2,3,4,5]
# l[-1]=500    #editing with indexing
# l[3]=777
# l[1:4]=[200,300,400]     #editing with slicing 
# print(l)

# DELETING ITEMS FROM A LIST;;
# l=[1,2,3,4,5]
# print(l)
# del l         #del
# print(l)

# l=[1,2,3,4,5]
# del l[-1]
# print(l)
# del l[1:3]
# print(l)

# l=[1,2,3,4,5]
# l.remove(5)       #remove
# print(l)

# l=[1,2,3,4,5]
# l.pop(4)   #pop
# print(l)

# l=[1,2,3,4,5]
# l.pop()   #pop
# print(l)

# l=[1,2,3,4,5]
# l.clear()   #clear
# print(l)

# OPERATIONS ON LISTS;;
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print(l1+l2)    #arithmetic
# print(l1*3)     #repitition
# print(l2*2)

# l1=[1,2,3,4,5]
# l2=[1,2,3,4,[5,6]]
# print(5 in l1)    #membership
# print(5 not in l2)

# l1=[1,2,3,4,5]
# l2=[1,2,3,4,[5,6]]
# for i in l1:    #through loop
#     print(i)
# for i in l2:
#     print(i)

# LIST FUNCTIONS:
# l=[1,2,3,4]
# print(len(l))    #Len
# print(min(l))    #min
# print(max(l))     #max
# print(sorted(l,reverse=True))    #sorted

# l=[1,2,3,4,1,2,3,3]
# print(l.count(1))   #count
# print(l.index(3))   #index 

# l=[1,2,3,4]
# print(l.reverse())   #reverse
# print(l)

# l=[2,1,5,7,0]    #sorted vs sort
# print(l)
# print(sorted(l))
# print(l)
# print(l.sort())
# print(l)

# l=[1,2,3,4,4]
# print(id(l))
# l1=l.copy()
# print(l1)
# print(id(l1))

# Q-1.WAP ADD 1 TO 10 NUMBERS IN A LIST?
# l=[]
# for i in range(1,11):
#     l.append(i)
# print(l)

# THROUGH LIST COMPREHENSIONS;;
# l=[i for i in range(1,11)]
# print(l)

# Q-2 WAP SCALAR MULTIPLICATION ON A VECTOR?
# v=[2,3,4]
# s=-3
# print([s*i for i in v])

# ADD SQUARES;;
# l=[1,2,3,4,4]
# print([i**2 for i in l])

# Q-3 WAP PRINT ALL NUMERS DIVISIBLE BY 5 IN THE RANGE OF 1 TO 50?
# print([i for i in range(1,51) if i%5 ==0])

# Q-4 WAP TO FIND LANGUAGES WHICH START WITH LETTER P?
# languages=['Java','Python','Php','C',"Javascript"]
# print([languages for languages in languages if languages.startswith('P')])

# Q-5 WAP ADD NEW LIST FROM MY_FRUITS AND ITEMS IF THE FRUITS EXITS IN BASKET AND ALSO STARTS WITH 'A'?
# basket=['Apple','Guava','Cherry','Banana']
# my_fruits=["Apple",'Kiwi','Grapes','Banana']
# print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith("A")])

# Q-6 WAP(3,3)MATRIX USING LIST COMPREHENSION?
# print([[i*j for i in range(1,4)] for j in range(1,4)])

# Q-7 WAP ON CARTESIAN PRODUCTS 2 LIST TOGETHER INTO LIST COMPREHENSION?
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print([i*j for i in l1 for j in l2])

# TRAVERSE A LIST;;
# l=[1,2,3,4,4]
# for i in l:   #itemwise loop
    # print(i)

# l=[1,2,3,4]
# for i in range(0,len(l)):    #indexwise loop
#     print(i)

# Q-8 WAP TO ADD ITEMS OF LIST TWO NUMBERS USING ZIP?
# l1=[1,2,3,4]
# l2=[-1,-2,-3,-4]
# list(zip(l1,l2))
# print([i+j for i,j in zip(l1,l2)])

# MUTABILITY IN LISTS;
# a=[1,2,3]
# b=a.copy()
# print(a)
# print(b)
# a.append(4)
# print(a)
# print(b)