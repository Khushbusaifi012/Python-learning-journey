# ATM MACHINE CONCEPTS;;
class Atm:
    def __init__(self):    #constructor
        self.pin=""
        self.balance=0
        print("Executed it")
        self.menu()
        
    def menu(self):
        user_input=input("""
        Hi how can i help you?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3. Press 3 to check balance
        4.Press 4 to withdraw
        5.Anything else to edit        
        """)
    
        if user_input=="1":   #create pin
            self.create_pin()
        
        elif user_input=="2":      #change pin
            self.change_pin()

        elif user_input=="3":    #check balance
            self.check_balance()
        elif user_input=="4":    #withdraw balance
            self.withdraw()
        else:     
            exit()
        
    def create_pin(self):
        user_pin=input("Enter ur pin :")
        self.pin=user_pin
        user_balance=int(input("Enter balance : "))
        self.balance=user_balance
        print("pin created successfully!!")
        self.menu()

    def change_pin(self):
        old_pin=input("Enter old pin : ")
        if old_pin==self.pin:    #let him change the pin
            new_pin=input("Enter new pin :")
            self.pin=new_pin
            print("Pin has changed successfully!!")
            self.menu()
        
        else:
            print("not to be changed!!")
            self.menu()

    def check_balance(self):
        user_pin=input("Enter ur pin :")
        if user_pin==self.pin:
            print("Your balance is : ",self.balance)
        else:
            print("Pin is incorrect")

    def withdraw(self):
        user_pin=input("Enter the pin : ")
        if(user_pin==self.pin):    #allow to withdraw
           amount=int(input("Enter the amount : "))
           if amount<=self.balance:
               self.balance=self.balance=amount
               print("Withdrawl successfull balance is : ",self.balance)          
           else:
               print("You are poor")       

        else:
            print("Password is incorrect")
            self.menu()
    
obj=Atm()    #create an object
print(type(obj))     

# PRINT HELLO;;
class temp:
    def __init__(self):
        print("Hello")
obj=temp()

# MAKE A FRACTION WAY USING MAGIC METHODS;;
class Fraction:
    def __init__(self,x,y):       #parameterized constructor
        self.num=x
        self.den=y
    
    def __str__(self):   #magic methods
        return '{}/{}'.format(self.num,self.den)    
    
    def __add__(self,other):   #add function in fractions
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den) 
    
    def __sub__(self,other):   #sub function in fractions
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den) 
    
    def __mul__(self,other):   #multiply function in fractions
        new_num=self.num*other.num
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den) 
    
    def __truediv__(self,other):   #div function in fractions
        new_num=self.num*other.den
        new_den=self.den*other.num
        return '{}/{}'.format(new_num,new_den) 
    
    def convert_to_decimal(self):    #convert to decimal
        return self.num/self.den

f1=Fraction(1,2)
f2=Fraction(4,5)
print(f1)
print(f2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1.convert_to_decimal())