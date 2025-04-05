
# CASE-1 IF THE FILE IS NOT PRESENT;;
# f=open('sample.txt','w')
# f.write('Hello world')
# f.close()    #since file is closed hence this will not work
# f.write('Hello')

# WRITE MULTIPLINE STINGS;;
f=open('sample1.txt','w')
f.write('Hello world')
f.write('\n \How are you? ' )
f.close()

# CASE-2 IF THE FILE IS ALREADY PRESENT;;
f=open('sample1.txt','w')
f.write('Khushbu')
f.close()

# PROBLEM WITH W CODE,INTRODUCING APPEND MODE;;
f=open('sampe1.txt','a')
f.write('\nI am fine')
f.close()

# WRITE LINES;;
l=['hello\n','hi\n','how are you\n','i am fine\n']
f=open('sample.txt','w')
f.writelines(l)
f.close()

# READING FROM FILES USING READ;;
f=open('sample.txt','r')
s=f.read()
print(s)
f.close()

# READING UPTO N CHARS;;
f=open('sample.txt','r')
s=f.read(10)
print(s)
f.close()

# READLINES()--->TO READ LINE BY LINE;;
f=open('sample.txt','r')
print(f.readline(),end='')    #line by line reading content
print(f.readline(),end='')
f.close()

# READING ENTIRE USING READLINE;;
f=open('sample.txt','r')
while True:
    data=f.readline()
    if(data==''):
        break
    else:
        print(data,end='')
f.close()

# WITH KEYWORD;;
with open('sample1.txt','w') as f:
    f.write('khushbu saifi')
# f.write('hello')   #closed the file automatically

# TRY F.READ() NOW;
with open('sample1.txt','r') as f:
    print(f.read())

# MOVING WITHIN A FILE ->10 CHAR THEN 10 CHAR;;
with open('sample.txt','r')as f:
    print(f.read(10))
    print(f.read(10))

# BENEFIT?->TO LOAD A BIG FILE IN MEMORY;;
big_l=['hello world' for i in range(100)]
with open('big.txt','w') as f:
    f.writelines(big_l)
with open('big.txt','r')as f:
    chunk_size=10
    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end='***')
        f.read(chunk_size)

# SEEK AND TELL FUNCTION;;
with open('sample.txt','r') as f:
    print(f.read(10))
    print(f.tell())
    f.seek(0)
    print(f.read(10))
    print(f.tell())

# SEEK DURING WRITE;;
with open('sample.txt','w') as f:
    f.write('hello')
    f.seek(0)
    f.write('x')

# WORKING WITH BINARY FILE;;
with open('th.jpeg','rb')as f:
    with open('th.copy.jpeg','wb')as wf:
        wf.write(f.read())

# WORKING WITH OTHER DATA TYPES;;
d={
    'name':'khushbu',
    'age':20,
    'gender':'female'
}
with open('sample.txt','w')as f:
    f.write(str(d))

# SERIALIZATION USING JSON MODULE IN LIST;;
import json
l=[1,2,3,4]
with open('demo.json','w')as f:
    json.dump(l,f)

# DICT;;
d={
    'name':'bhupi',
    'age':25,
    'gender':'male'
}
with open ('demo.json','w')as f:
    json.dump(d,f,indent=4)

# DESERIALIZATION;;
import json
with open('demo.json','r')as f:
    d=(json.load(f))
    print(d)
    print(type(d))

# SERIALIZE AND DESERIALIZE TUPLE;;
import json
t=(1,2,3,4,5)
with open('demo.json','w')as f:
    json.dump(t,f)   #it will always give list data type

# SERIALIZE AND DESERIALIZE CUSTOM OBJECTS;;
class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender

person=Person('Khushbu','saifi',20,'female')
import json     #as a string
def show_object(person):
    if isinstance(person,Person):
        return '{}-> {} age -> gender -> {}'.format(person.fname,person.lname,person.age,person.gender)
with open('demo.json','w')as f:
    json.dump(person,f,default=show_object)

# PICKLING;;
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_info(self):
        print('hi my name is ',self.name,'and i am',self.age,'years old')

p=person('khushbu',20)
import pickle   #pickle dump
with open('person.pkl','wb')as f:
    pickle.dump(p,f)
import pickle  #pickle load
with open('person.pkl','rb')as f:
    p=pickle.load(f)
p.display_info()

