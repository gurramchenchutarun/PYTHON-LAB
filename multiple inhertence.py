class A:
    def methodA(self):
        print('method A')
class B:
    def methodB(self):
        print('method B')
class C(A,B):
    pass
c=C()
c.methodA()
c.methodB()
