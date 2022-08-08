class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def about_Son(self):
        print('Grandfather name:', self.grandfathername)
        print('Father name:', self.fathername)
        print('Son name:', self.sonname)


object1 = Son('Abrorbek', 'Akbarjon', 'Latipboy')
object1.about_Son()



# class Parent:
#     def func1(self):
#         print('This is function in class Parent')
#
# class Child1(Parent):
#     def func2(self):
#         print('This is funtion in class Child 1')
#
# class Child2(Child1):
#     def func3(self):
#         print('This is funtion in class Child 2')
#
# object2 = Child2()
# object2.func2()







