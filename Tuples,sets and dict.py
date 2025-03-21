# CREATING TUPLES;;
# t1=()
# print(t1)   #empty tuple

# CREATE A TUPLE WITH A SINGLE ITEM;;
# t2=("Hello",)
# print(t2)
# print(type(t2))

# t3=(1,2,3,4)
# print(t3)

# t4=(1,2.5,True,[1,2,3])
# print(t4)

# t5=(1,2,3,(4,5))
# print(type(t5))

# t6=tuple("Khushbu")    #using type conversion
# print(t6)

# HOW TO ACCESS ITEMS IN A TUPLE;;
# t=(1,2,3,4,5)
# print(t)
# print(t[0])
# print(t[-1])    #indexing
# print(t[3:4])
# print(t[1:3])    #slicing

# HOW TO EDIT ITEMS IN A TUPLE;;
# t=(1,2,3,4,5,6,7)
# print(t)
# t[0]=100
# print(t)     #this method will give us error because tuple is immutable once is created we cannot modify it..

# HOW TO ADDING ITEMS IN A TUPLE;;
# t=(1,2,3,4,5,66)
#IN THIS CASE ALSO WE CANNOT ADDING ITEMS IN A LIST

# HOW TO DELETING ITEMS IN A LIST?
# t=(1,2,3,4,5,5,6)
# del t
# print(t)

# OPERATIONS ON TUPLES;;
# t1=(1,2,3,4)
# t2=(2,3,4,5)
# print(t1+t2)     #addition
# print(t1*3)      #repetition
# print(1 in t1)
# print(6 not in t2)    #membership
# for i in t1:        #loops
#     print(i)

# TUPLE FUNCTIONS;;
# t=(1,2,3,4,5,2,2,2,2)
# print(len(t))         #len function
# print(sum(t))         #sum
# print(min(t))         #min
# print(max(t))          #max
# print(sorted(t,reverse=True))        #sorted
# print(t.count(2))            #count
# print(t.index(5))            #index

# WHY LIST TAKES MORE TIME TO EXECUTE AS COMPARED TO TUPLES?
# import time
# l=list(range(10))
# t=tuple(range(10))
# start=time.time()
# for i in l:
#     i*5
# print("List time : ",time.time()-start)
# start=time.time()
# for i in t:
#     i*5
# print("Tuple time : ",time.time()-start)

# WHY LIST TAKE MORE SIZE AS COMPARED TO TUPLES?
# import sys
# l=list(range(100))
# t=tuple(range(100))
# print("List size  : ",sys.getsizeof(l))
# print("Tuple size  : ",sys.getsizeof(t))

# WHY USE TUPLES?
# a=(1,2,3)
# b=a
# a=a+(4,)
# print(a)
# print(b)

# TUPLE UNPACKING;;
# a,b,c=(1,2,3)
# print(a,b,c)

# SWAPPING TUPLES;;
# a=1
# b=2
# a,b=b,a
# print(a,b)

# a,b,*others=(1,2,3,4)
# print(a,b)
# print(others)

# ZIPPING TUPLES;;
# a=(1,2,3,4)
# b=(5,6,7,8)
# print(tuple(zip(a,b)))

# SETS;;
# s={}       
# print(type(s))

# s=set()             #empty set
# print(type(s))   

# s={1,2,3,}             #1d set
# print(s)

# s={1,2,3,{4,5}}
# print(s)

# s={1,"hello",10.5,False}    #heterogeneous
# print(s)

# s=set([1,2,3,4,5])     #type conversion
# print(s)  

# s={1,2,2,1,1,3}        #duplicates are not allowed
# print(s)

# s1={1,2,3,4}
# s2={4,3,2,1}
# print(s1==s2)     #ordered type

# HOW TO ACCESS ITEMS IN A SET?
# s1={1,2,3,4}
# print(s1[0])     #not applicable

# HOW TO EDIT ITEMS IN A SET?
# s1={1,2,3,4}
# s1[0]=100
# print(s1)    #not supported

# HOW TO ADD ITEMS IN SET?
# s={1,2,3,4}
# s.add(5)    #add
# print(s)

# s={1,2,3,4,5}
# s.update([5,6,7,8,9])    #update 
# print(s)

# HOW TO DELETE ITEMS IN A LIST?
# s={1,2,3,4,5,5,6,7,8,9}
# print(s)
# del s              #del
# print(s)

# s={1,2,3,4,5}
# s.discard(5)   #discard
# print(s)

# s={5,6,8,4}
# s.remove(5)     #remove
# print(s)

# s={1,2,3,4,5,6,7,8}
# s.pop()       #pop
# print(s)

# s={1,2,3,4,5,6}
# s.clear()       #clear
# print(s)

# # SET OPERATION;;
# s1={1,2,3,4,5,6,7}
# s2={2,3,4,6,7,8,9}
# print(s1 | s2)      #union
# print(s1 & s2)      #intersection
# print(s1-s2)
# print(s2-s1)       #difference
# print(s1^s2)        #symmetric difference
# print(1 not in s1)
# print(7 in s2)      #membership
# for i in s1:          #loops
#     print(i)

# SET FUCNTIONS;;
# s={1,2,3,4,5,6}
# print(len(s))    #len
# print(min(s))    #min
# print(max(s))     #max
# print(sum(s))     #sum
# print(sorted(s,reverse=True))   #sorted

# SET OPERATIONS WITH UPDATE;;
# s1={1,2,3,4,5,6}     
# s2={3,4,6,8,9}
# print(s1.union(s2))    #union and update
# s1.update(s2)
# print(s1)
# print(s2)

# s1={1,2,3,4,5,6}     
# s2={3,4,6,8,9}
# print(s1.intersection(s2))
# s1.intersection_update(s2)     #intersection and update
# print(s1)
# print(s2)

# s1={1,2,3,4,5,6}     
# s2={3,4,6,8,9}
# print(s1.difference(s2))
# s1.difference_update(s2)     #difference and update
# print(s1)
# print(s2)

# s1={1,2,3,4,5,6}     
# s2={3,4,6,8,9}
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)     #symmetric_difference and update
# print(s1)
# print(s2)

# s1={1,2,3,4}
# s2={5,6,7,8}
# print(s1.isdisjoint(s2))      #isdisjoint

# s1={1,2,3,4,5}
# s2={3,4,5}
# print(s2.issubset(s2))         #issubset

# s1={1,2,3,4,5}
# s2={6,7,8}
# print(s1.issuperset(s2))         #issuperset

# s1={1,2,34}
# s2=s1.copy()           #copy function
# print(s1)
# print(s2)

# FROZENSET;;
# fs=frozenset([1,2,3,4])
# print(fs)

# fs=frozenset([1,2,3,4,frozenset([3,4])])   #2d sets
# print(fs)

# SETS COMPREHENSION;;
# print({i for i in range(1,11)})

# DICTIONARY;;
# d={}      #empty dict
# print(type(d))
# d1={"name":"khushbu","Age":20,"gender":"Female"}   #homogeneous
# print(d1)
# d2={(1,2,3):1,"hello":"khushbu"}
# print(d2)
# s={           #2d dict
#     "name":"khushbu",
#     "college":"Bit",
#     "sem":4,
#     "subjects":{
#         'dsa':50,
#         "maths":40,
#         "english":89
#     }
# }
# print(s)
# d4=dict([(1,2),(2,2),(3,4)])    #using sequence and dict function
# print(d4)
# d5={"name":'k',"name":'k'}    #duplicate keys
# print(d5)
# d6={"name":"k",(1,2,3):2}         #mutable items as keys
# print(d6)

# HOW TO ACCESS ITEMS IN A LIST;;
# my_dict={"name":"khushbu","age":20}
# print(my_dict['age'])
# print(my_dict.get('name'))

# HOW TO ADD KEY VALUE PAIR IN A DICT?
# my_dict={"name":"khushbu","age":20}
# my_dict["gender"]="female"
# print(my_dict)

# HOW TO REMOVE KEY VALUE PAIR IN A DICT?
# d={"name":"khushbu","age":20,"gender":"female"}
# d.pop("age")    #pop
# print(d)

# d={"name":"khushbu","age":20,"gender":"female"}
# d.popitem()    #popitem
# print(d)

# d={"name":"khushbu","age":20,"gender":"female"}
# del d['name']   #del
# print(d)

# d={"name":"khushbu","age":20,"gender":"female"}
# d.clear()      #clear
# print(d)

# DICTIONARY OPERATIONS;;
# d={"name":"khushbu","age":20,"gender":"female"}
# print("Khushbu"  in d)   #membership operator 
# print("name" in d)   #loops
# for i in d:
#     print(i,d[i])

# DICTIONARY FUNCTIONS;;
# d={"course":"Btech","college":"amity","location":"noida"}
# print(len(d))   #len
# print(sorted(d,reverse=True))    #sorted
# print(min(d))    #min
# print(max(d))    #max
# print(d.items())    #itens
# print(d.keys())
# print(d.values())

# d1={1:2,3:4,5:6}
# d2={4:7,6:8}
# d1.update(d2)     #update
# print(d1)  

# USING DICT COMPREHENSION;;
# Q.1 WAP TO PRINT 1ST TO 10 NUMBERS AND THEIR SQUARES?
# print({i:i**2 for i in range(1,11)})

# Q.2 WAP TO PRINT USING EXISTING DICT?
# d={'delhi':1000,'mumbai':2000,'bangalore':3000}
# print({key:value*0.62 for (key,value) in d.items()})

# Q.3 WAP TO PRINT USING ZIP?
# days=["s","m","t","w","t","f","s"]
# d=[30.5,32.6,31.8,33.4,29.5,30.2,29.9]
# print({i:j for (i,j) in zip(days,d)})

# # Q.4 WAP TO PRINT USING IF CONDTION?
# product={"phone":10,"laptop":0,"charger":32,"tablet":3}
# print({key:value for (key,value) in product.items() if value > 0})

# Q.5 WAP TO PRINT TABLES OF NUMBER FROM 2 TO 4? USING LIST COMPREHENSION;
# print({i:{j:i*j for j in range(1,11)}for i in range(2,5)})

