'''class student:
    def __init__(self,name,rollno):
        #instance variables created inside constructor using self
        self.name=name
        self.rollno=rollno
        print("inside constructor:")
        print("Name:",self.name)
        print("Roll no:",self.rollno)

    def update__marks(self,marks):
        #instance variable craated /modified inside method using self
        self.marks=marks
        print("\ninside instance method")
        print(f"{self.name}'s marksupdate to:",self.marks)
#creating object of student
s1=student("Anil",101)
#accessing and modifying instance variables from outside the class using object refreence
print("\nOutside of class:")
print("Name(before):",s1.name)
#modifying instance variable
s1.name="Anil kumar"
print("Name(after):",s1.name)
#calling instance method to add/update marks
s1.update__marks(85)
#accessing newly added instance variable(marks) from outside
print("marks(outside):",s1.marks)'''

#deleting instance variable
class employee:
    def __init__(self,name,emp_id):
        self.name=name;
        self.emp_id=emp_id;
        self.salary=50000
        print("constructor initilized")
        print(self.__dict__)

    def remove_salary(self):
            #deleting insatnace variable within a class
            del self.salary
            print("\nAfter deleting'salary'within class:")
            print(self.__dict__)
#create object
e1=employee("Anil kunmar",1001)
#deleting instance variable from outside the class
del e1.emp_id
print("\nAfter deleting'emp_id' from outside class:")
print(e1.__dict__)
#call method to delete 'salary' from within class
e1.remove_salary()
