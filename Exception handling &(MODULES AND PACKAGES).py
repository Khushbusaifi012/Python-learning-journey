# EXAMPLES OF SyntaxError;;
# Print 'hello world'    # it is a invalid syntax

# a=5
# if a==2
#      print('hello')

# a=3
# if a==3:
# print('hey')

# INDEX ERROR;;
# l=[1,2,3,4,5]
# l[100]

# MODULENOTFOUNDERROR;;
# import mathi    #it will give a error
# math.floor(4)

# KEYERROR;;
# d={'name':'khushbu'}
# d['age']

# TYPEERROR;;
# 1+'a'

# VALUERROR;;
# int('a')
# print(type('a'))

# NAMEERROR;;
# print(k)

# ATTRIBUTEERROR;;
# l=[1,2,3,4]
# l.upper()

# LETS CREATE A FILE;;
with open('sample.txt','w')as f:
    f.write('hello pythoniasts')
try:
  with open('sample.txt','r')as f:   #try catch demo
    print(f.read())
except:
   print('Sorry file not found!!')   #if we give a wrong file name 

# CATCHING SPECIIC EXCEPTION;;
try:
  k=5
  f=open('sample.txt','r')
  print(f.read())
  print(k)
  print(5/2)
  l=[1,2,3]
  l[100]
except FileNotFoundError:
   print('file not found')
except NameError:
   print('variable not defined')
except ZeroDivisionError:
   print('cant divide by 0')
except Exception as e:   #generic block
   print(e)

# ELSE BLOCK;;
try:
  f=open('sample.txt','r')
except FileNotFoundError:
  print("File not found")
except Exception:
  print('Something has issue')
else:   #if try block has not problem
  print(f.read())

# FINALLY BLOCK;;
try:
  f=open('sample.txt','r')
except FileNotFoundError:
  print("File not found")
except Exception:
  print('Something has issue')
else:   #if try block has not problem
  print(f.read())
finally:
  print('this is to be print')

# RAISE EXCEPTION;;
# raise NameError('just trial')
# raise FileNotFoundError('file not found')

class bank:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self,amount):
        if (amount<0):
            raise Exception('Amount cannot be negative')
        if self.balance<amount:
            raise Exception('U have not money')
        self.balance=self.balance-amount

obj=bank(10000)
try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)

# CUSTOM EXCEPTIONS;;
class Myexception(Exception):
    def __init__(self,message):
      print(message)

class bank:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self,amount):
        if (amount<0):
            raise Myexception('Amount cannot be negative')
        if self.balance< amount:
            raise Myexception('U have not money')
        self.balance=self.balance-amount

obj=bank(10000)
try:
    obj.withdraw(5000)
except Myexception as e:
    print(e)
else:
    print(obj.balance)

# SIMPLE EXAMPLE;;
class Securityerror:
    def __init__(self,message):
        print(message)
    
    def logout(self):
        print('logout')
        
class google:
    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device
    
    def login(self,email,password,device):
        if device!=self.device:
            raise Securityerror('all acc are hacked')
        if email==self.email and password ==self.password:
            print('welcome')
        else:
            print('login error')

obj=google('gmail','gmail27@.com',123445,'Iphone')

try:
    obj.login('gmail27@.com',123445,'Iphone')
except Securityerror as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connection closed')   