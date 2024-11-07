class vector_2:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")   


class vector_3:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def show(self):
        print(f"the vector is {self.i}i + {self.j} + {self.k}k")            

a=vector_2(1,2)
a.show()
b=vector_3(1,2,3)
b.show()        