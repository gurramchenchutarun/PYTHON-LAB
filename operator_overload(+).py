'''class Point:#+ operator overloading
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
p1=Point(1,2)
p2=Point(3,4)
p3=Point(0,0)
p3=p1+p2
print(p3)'''
#==,operator overload
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __eq__(self,other):
        return self.roll==other.roll,self.name==other.name
s1=Student("Anil",101)
s2=Student("Ravi",101)
print(s1==s2)
