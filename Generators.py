import sys
sys.getsizeof(2)
x=range(100)
for i in x:
    print(i**2)
sys.getsizeof(x)

# A SIMPLE EXAMPLE;;
def gen_demo():
    yield'First statement'
    yield'second statement'
    yield'third statement'

gen=gen_demo()
print(next(gen))
print(next(gen))
print(next(gen))

# EXAMPLE-2;;
def square(num):
    for i in range(1,num+1):
        yield i**2
gen=square(10)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

# RANGE FUNCTION USING GENERATOR;;
def my_range(start,end):
    for i in range(start,end):
        yield i

gen=my_range(15,25)
for i in gen:
    print(i)

# GENERATOR EXPRESSION;;
# l=[i**2 for i in range(1,101)]   #list comprehension
gen=(i**2 for i in range(1,101))
for i in gen:
    print(i)

# BENEFITS OF USING A GENERATOR;;
# 1.EASE OF IMPLEMENTATION--->>
def my_range(start,end):
    for i in range(start,end):
        yield 1

# 2.MEMORY EFFICIENT--->>
l=[x for x in range(100)]
gen=(x for  x in range(100))
import sys
print('Size of L in memory : ',sys.getsizeof(l))
print('Size of gen in memory : ',sys.getsizeof(gen))

# 3.REPRESENTING INFINITE STREAMS;;
def all_even():
    n=0
    while True:
        yield n
        n+=2
even_num_gen=all_even()
print(next(even_num_gen))
print(next(even_num_gen))
print(next(even_num_gen))

# CHAINING GENERATORS;;
def fibonacci_numbers(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(list(square(fibonacci_numbers(10))))