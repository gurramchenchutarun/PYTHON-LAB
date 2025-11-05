'''for i in range(10):
    if i%2==0:
        continue
    print(i)'''
numbers=[10,20,0,5,0,30]
for n in numbers:
    if n==0:
        print("how can we divide with zero....skip")
        continue
    print("100/{}={}".format(n,100/n))
