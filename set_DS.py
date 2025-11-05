#set data structures,[doesnot allow duplicate elements]
#insertion order is not preserved
#curly braces were used
'''s={10,20,30,40}
print(s)
print(type(s))
s={}
print(s)
print(type(s))
#add(),adds 1 item to set
#s.add();'''

#update(x,y,z),add multiple items to set
'''s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)'''

'''#copy(),copy one set to another
s={10,20}
s1=s.copy()
print(s1)'''
#pop(),remove and return some random element
'''s={40,10,30,20}
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)'''

#remove(x),removes specified element
'''s={10,20,30}
s.remove(20)
print(s)'''
#disard(x),removes specified element from set
'''s={10,20,30}
s.discard(50)
print(s)'''

#clear(),remove elements from set
'''s={10,20,30}
s.clear()
print(s)
'''
#union(),to dispaly all elements in both sets ,removing duplicate elements
'''s={10,20,30}
r={20,30,40}
print(s.union(r))'''
#intersection(),return common elements(&)
'''s={10,20,30}
r={20,30,40}
print(s.intersection(r))'''

#difference(),x.diffference(Y),returns only x elements(x-y)
'''s={10,20,30}
r={20,30,40}
print(s.difference(r))'''
#symmetric_difference(),displays which are not common
'''s={10,20,30}
r={20,30,40}
print(s.symmetric_difference(r))'''


