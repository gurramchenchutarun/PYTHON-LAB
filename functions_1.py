#function
#example
'''def display():
    print("hello")
display()#calling a function'''
#exm 2
'''def sum(a,b):
    c=a+b
    print(c)#or we can write return type
sum(10,20)'''
#or we can write return type
'''def sum(a,b):
    c=a+b
    return c
print(sum(10,20))'''
#sum and difference
def sum(a,b):
    c=a+b
    d=a-b
    return c,d
print(sum(30,20))
