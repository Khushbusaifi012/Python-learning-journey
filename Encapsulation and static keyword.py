"""QUESTION POINTS 1.A user can create and view 2d coordinates
   2.A user can find out the distance between 2 coordinates
   3.A user can find the distance of a coordinate from origin
   4.A user can check if a point lies on a given line
   5. A user can find the distance between a given 2d point and a given line
"""
class Point:
    def __init__(self,x,y):    #parameterized constructor
        self.x_cod=x
        self.y_cod=y
    
    def __str__(self):
        return ('<{},{}>' .format(self.x_cod,self.y_cod))
    
    def eucliedan_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 +(self.y_cod-other.y_cod)**2)**0.5
    
    def distance_rom_origin(self):
        return self.eucliedan_distance(Point(0,0))
    
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    
    def __str__(self):
        return '{}x +{}y + {} =0'.format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
       if(line.A*point.x_cod + line.B*point.y_cod +line.C==0):
           return "Lies on the line"
       else:
           return "Does not lie on the line" 
    
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod +line.B*point.y_cod +line.C)/(line.A**2 +line.B**2)

p1=Point(2,1)
p2=Point(4,10)
l1=Line(3,4,5)
print(p1)
print(p2)    
print(p1.eucliedan_distance(p2))
print(p1.distance_rom_origin())
print(l1)
print(l1.point_on_line(p1))
print(l1.shortest_distance(p1))

# QUESTION -2 HOW OBJECTS ACCESS ATTRIBUTES;;
class Person:
    def __init__(self,name_input,country_input):
        self.name=name_input
        self.country=country_input

    def greet(self):
        if(self.country=="India"):
            print("Namaste",self.name)
        else:
             print("Hello",self.name)

p=Person("Khushbu",'India')    #how to access attributes
print(p.name)
print(p.country)     
p.greet()           #how to access methods
p.gender="female"       #attribute creation from outside of the class
print(p.gender)

# QUESTION-3 OBJECTS WITHOUT A REFERENCE;;
class Person:
    def __init__(self):
        self.name="Saniya"
        self.gender="female"
p=Person()
q=p
print(id(p))     #multiple reference
print(id(q))
print(p.name)
print(q.name)
q.name="Ankit"
print(q.name)
print(p.name)

# QUESTION-4 PASS BY REFERENCE;;
class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
def greet(person):    #outside the class --->function
    print("Hi my name is ",person.name,"And i am a ",person.gender)
    print(id(person))
    p1=Person("Shaheen","female")
    return p1

p=Person("Khushbu","Female")
x=greet(p)
print(x.name)
print(x.gender)
print(id(p))

# ENCAPSULATION INSTANCE VARIABLE;;
class person:
    def __init__(self,name_input,country_input):
        self.name=name_input
        self.country=country_input

p1=person("Khushbu","India")
p2=person("Steve","America")     
print(p1.name)    
print(p2.country)       

# LIST OF OBJECTS;;
class person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

p1=person("Khushbu","female")
p2=person("Abhi","male")
p3=person("Ankit","Male")
l=[p1,p2,p3]
print(l)
for i in l:
    print(i.name,i.gender)

# USING DICT;;
class person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

p1=person("Khushbu","female")
p2=person("Abhi","male")
p3=person("Ankit","Male")
d={"p1":p1,'p2':p2,"p3":p3}
print(d)
for i in d:
    print(d[i].name)
    print(d[i].gender)