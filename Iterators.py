# WHAT IS AN ITERATION?
l=[1,2,3]
for i in l:
    print(i)

# WHAT IS AN ITERATOR?
l=[x for x in range(1,100)]
for i in l:
    print(i*2)
import sys
print('time taken:',sys.getsizeof(l))

# WHAT IS ITERABLE;;
l=[1,2,3,4]
print(type(l))  #-->l is in an iterable     
print(type(iter(l)))       #-->iter(l)is an iterator

# HOW TO FIND THE OBJECT IS ITERABLE OR NOT?
t=(1,2,3)
print(dir(t))     #if we find iter is avaiable then the object is iterable
s={1,2,3}
print(dir(s))
d={'name':'khushbu','age':20}
print(dir(d))

# HOW TO FIND THE OBJECT IS ITERATOR OR NOT?
l=[1,2,3]
print(dir(l))  #l is not iterator
print(dir(iter(l)))    #it is an iterator because we find in iter and next

# UNDERSTANDING HOW FOR LOOP WORKS;;
num=[1,2,3]
for i in num:
    print(i)

num=[1,2,3]
iter_num=iter(num)    #fetch the iterator
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))

# MAKING OUR OWN LOOP;;;
def my_loop(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

a=[1,2,3,4]
b=range(1,11)
c=(1,2,3)
d={1,2,3,}
e={0:1,2:2}
my_loop(a)
my_loop(b)
my_loop(c)
my_loop(d)
my_loop(e)

# A CONFUSING POINT;;
num=[2,3,4]
iter_obj=iter(num)
print(id(iter_obj),'Address of iterator 1')
iter_obj2=iter(iter_obj)
print(id(iter_obj2),'Address of iterator 2')

# LETS CREATE OUR OWN RANGE FUNCTION;;;
class my_range():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    pass
    
    def __iter__(self):
        return my_range_iterator(self)
    
class my_range_iterator():
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start>=self.iterable.end:
            raise StopIteration
        current=self.iterable.start
        self.iterable.start+=1
        return current

x=my_range(1,11)
print(type(x))
print(iter(x))
for i in my_range(1,11):
    print(i)    