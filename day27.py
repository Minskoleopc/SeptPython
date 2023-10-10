class A(object):
    def method(self):
        print("A is called") # 3
        super().method()

class B(object):
    def method(self):
        print("B is called") # 5
        super().method()

class C(object):
    def method(self):
        print("C is called") # 6

class X(A,B):
    def method(self):
        print("X is called") # 2
        super().method()

class Y(B,C):
    def sham(self):
        print("Y is called") # 4
        super().method()

class P(X,Y,C):
    def ram(self):
        print("P is called") # 1
        super().method()

p = P()
p.ram()


# pilymorphism















