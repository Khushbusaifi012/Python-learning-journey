# AGGREGATION(HAS-A-RELATIONSHIP);;;
class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
  
class Address:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
    
    def get_city(self):     #use getter method if we want to access private methods
        return self.__city

add1=Address("gurgaon",1220111,"haryana")
cust=customer("Khushbu","female",add1)
print(cust.print_address())

# INHERITANCE EXAMPLE;;
class user:    #parent class
    def __init__(self):
        self.name="khushbu"
    
    def login(self):
        print("Login")

class student(user):     #child class
    def enroll(self):
        print("Enroll into the course")

u=user()
s=student()
print(s.name)
s.login()
s.enroll()

# CONSTRUCTOR EXAMPLE 1;;
class phone:    #parent class
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")
    
class smartphone(phone):    #child class
    pass

s=smartphone(200000,"Apple",12)
s.buy()

# CONSTRUCTOR EXAMPLE 2;;
class phone:    #parent class
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    
class smartphone(phone):    #child class
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")

s=smartphone("Android",2)

# CHILD CLASS CAN'T ACCESS PRIVATE MEMBERS OF THE CLASS;;
class phone:    #parent class
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    def show(self):
        print(self.__price)

class smartphone(phone):    #child class 
    def check(self):
        print(self.__price)

s=smartphone(200000,"Apple",13)
print(s.brand)
# s.check()

# NEXT EXAMPLE-1;;
class parent:     #parent class
    def __init__(self,num):
        self.__num=num
    
    def get_num(self):    #getter method
        return self.__num

class child(parent):   #child class
    def show(self):
        print("This is in child class")
    
son=child(100)
print(son.get_num())
son.show()

# NEXT EXAMPLE-2;;
# class parent:    #parent class  
#     def __init__(self,num):
#         self.__num=num
    
#     def get_num(self):   #getter method
#         return self.__num

# class child(parent):    #child class
#     def __init__(self,val,num):  #child class has also constructor since parent class constrcutor will never be called.
#         self.__val=val
    
#     def get_val(self):   #getter method
#         return self.__val

# son=child(100,10)
# print("parent : Num :",son.get_num())
# print("child: val:",son.get_val())

# NEXT EXAMPLE-3;;
class A:    #parent class
    def __init__(self):    #child class has no constructor since this scenario parent class constructor will be called
        self.var1=100
    
    def display1(self,var1):
        print("Class A : ",self.var1)
    
class B(A):    #child class
    def display2(self, var1):
        print("Class B :",self.var1)

obj=B()
obj.display1(100)
obj.display2(120)

# NEXT EXAMPLE-4;;METHOD OVERRIDING;;
class phone:     #parent class
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):  #child class
    def buy(self):
        print("Buying a smartphone")
    
s=smartphone(200000,"Apple",12)
s.buy()

# SUPER KEYWORD;;
class phone:     #parent class
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):  #child class
    def buy(self):
        print("Buying a smartphone")
        super().buy()   #syntax to called parent buy method

s=smartphone(200000,"Apple",12)
s.buy()

# WHY WE USE SUPER METHOD?
class phone:     #parent class
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

class smartphone(phone):    #child class
    def __init__(self, price, brand, camera,os,ram):
        super().__init__(price, brand, camera)
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")
    
s=smartphone(200000,'Samsung',12,"Android",2)
print(s.os)
print(s.brand)

# CAN WE USE SUPER METHOD INTO OUTSIDE OF THE CLASS?
# class phone:     #parent class
#     def __init__(self,price,brand,camera):
#         print("inside phone constructor")
#         self.price=price
#         self.brand=brand
#         self.camera=camera

#     def buy(self):
#         print("Buying a phone")

# class smartphone(phone):  #child class
#     def buy(self):
#         print("Buying a smartphone")
        
# s=smartphone(200000,"Apple",12)
# s.super().buy()   #this is wrong to use super method always execute inside the class not in outside

# GET PRACTISE;;
class parent:
    def __init__(self,num):
        self.__num=num
    
    def get_num(self):
        return self.__num
    
class child(parent):
    def __init__(self, num,val):
        super().__init__(num)
        self.__val=val

    def get_val(self):
        return self.__val

son=child(100,200)
print(son.get_num())
print(son.get_val())

# GET PRACTISE;;
class parent:
    def __init__(self):
        self.num=100
    
class child(parent):
    def __init__(self):
        super().__init__()
        self.var=200
    
    def show(self):
        print(self.num)
        print(self.var)

son=child()
son.show()

# TYPES OF INHERITANCE;;;SINGLE;;
class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    pass
smartphone(100000,"Apple","13px").buy()

# MULTILEVEL INHERITANCE;;
class product:
    def review(self):
        print("Product customer review")
    
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    pass
s=smartphone(100000000,"Apple",12)
s.buy()
s.review()

# HIERARCHIAL INHERITANCE;;
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    pass
class featurephone(phone):
    pass
smartphone(1000,"Apple","13px").buy()
featurephone(10,"lava","12px").buy()

# MULITPLE INHERITANCE;;
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class product:
    def review(self):
        print("customer review")

class smartphone(phone,product):
    pass
s=smartphone(20000,'Apple',12)
s.buy()
s.review()

# THE DIAMOND PROBLEM;;
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class product():
    def buy(self):
        print("Product buy method")
    
class smartphone(phone,product):    #method resolution order 
    pass

s=smartphone(200000,"Apple",12)
s.buy()

# EXAMPLE;
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj3.m1()+obj3.m2())

# EXAMPLE;;
# class A:
#     def m1(self):
#         return 20

# class B(A):
#     def m1(self):
#         val=super().m1()+30
#         return val

# class C(B):
#     def m1(self):
#         val=self.m1()+20
#         return val

# obj=C()
# print(obj.m1())

# METHOD OVERLOADING;;
class shape:
    def area(self,radius):     #first method
        return 3.14*radius*radius
    
    def area(self,l,b):        #second method
        return l*b
s=shape()
s.area(2)
s.area(3,4)     #this will not be work