#default arguments
'''class Demo:
    def greet(self,name=None):
        if name:
            print(f"Hello,{name}!")
        else:
            print("Hello!")
obj=Demo()
obj.greet()
obj.greet("Anil")'''
#variable length arguments
class Calculator:
    def add(self,*args):
        return sum(args)
c=Calculator()
print(c.add(2))
print(c.add(2,3))
print(c.add(1,2,3))
