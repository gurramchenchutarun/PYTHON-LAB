class A:
    def methodA(self):
        print('A')
class B(A):
    def methodB(self):
        print('B')
class C:
    def methodC(self):
        print('C')
class D(B,C):
    pass
d=D()
d.methodA()
d.methodB()
d.methodC()
