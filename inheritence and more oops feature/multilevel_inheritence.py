class A:
    def print_1(self):
        print("hello1")

class B(A):
    def print(self):
        print("hello")

class C(B):
    pass


c=C()
c.print()
c.print_1()