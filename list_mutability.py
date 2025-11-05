'''n=[10,20,30,40]
print(n)
n[1]=777
print(n)'''

'''#accessing elments of lists usin index
l=[10,20,30,40]
print(l[0])
print(l[-1])
print(l[4])'''

'''#using slice operator,accessing multiple elements
#list[start(index of start):stop(index of stop(-1):step(increment)]
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])666
print(n[4:100])'''
'''#traversing the list by while loop
n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1'''
'''#traversing the list by while loop
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    print(n1)'''
'''#len()
n=[10,20]
print(len(n))'''
'''#count(),no of times element repeated
n=[1,2,2,3,3,3,4,4,4,4,5]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))'''
'''#index(),to get index of element
n=[1,2,2,3,3,3,4,4,4,4,5]
print(n.index(1))
print(n.index(2))
print(n.index(3))
print(n.index(4))
print(n.index(6))
#index(),to get index of element'''
"""n=[1,2,2,3,3,3,4,4,4,4,5]
x=int(input("enter a value:"))
if x in n:
    print(n.index(x))
else:
    print("not in list")"""
#append(),adds end of list
l=[]
l.append("A")
l.append("B")
l.append("C")
print(l)



