# dict(),d={} or d=dict()
'''d={}#first crete dictionary and then give values
d[100]="ram"
d[200]="sita"
print(d)'''

#access elements of dictionary,by using key values
'''d={100:'srinu',200:'ram'}
print(d[100])
print(d[400])'''

#update,in dictionaries ,d[key]=value
'''d={1:'ram',2:'sita',3:'ravan'}
print(d)
d[3]='laxman'
print(d)
'''
'''d={1:'ram',2:'sita',3:'ravan'}
print(d)
d[4]='sam'
print(d)
d[3]='laxman'
print(d)'''

#delete from dictionary,del d[key]
'''d={1:'ram',2:'sita',3:'ravan'}
print(d)
del d[1]
print(d)
del d[4]'''
#clear(),to remove all elements in dict,d.clear()
'''d={1:'ram',2:'sita',3:'ravan'}
print(d)
d.clear()
print(d)
'''
# to delete dict itself
'''d={1:'ram',2:'sita',3:'ravan'}
print(d)
del d
print(d)'''
#get(),d.get(key) or d.get(key,default value),if key not present key value will be displayed
d={1:'ram',2:'sita',3:'ravan'}
print(d)
print(d.get(1))
print(d.get(100))
print(d.get(100,"guest"))



