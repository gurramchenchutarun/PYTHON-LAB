class parent:
    def show(self):
        print('parent')
class Child1(parent):
    pass
class Child2(parent):
    pass
c1=Child1()
c2=Child2()
c1.show()
c2.show()
