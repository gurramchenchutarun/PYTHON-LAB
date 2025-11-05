class Student:
    def __init__(self,name=None,age=None):
        if name and age:
            print(f"Name:{name},Age:{age}")
        elif name:
            print(f"Name:{name}")
        else:
            print("NO details")
s1=Student()
s2=Student("Ravi")
s2=Student("Anil",20)
