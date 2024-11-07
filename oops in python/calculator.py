class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"square is {self.n*self.n}")

    def cube(self):
        print(f"cube is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"square root is {self.n**1/2}")   


p = calculator(4)
p.square()
p.cube()
p.square_root()
