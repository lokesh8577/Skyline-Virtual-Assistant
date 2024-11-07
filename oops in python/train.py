import random
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"your train ticket is booked and your train number is {self.trainNo} from {fro} to  {to}")

    def getstatus(self):
        print(f"train no : {self.trainNo} is running on time")

    def getfar(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(2,777)}")


t=train(13144)
t.book('bhilwara','jaipur')
t.getstatus()
t.getfar('bhilwara','jaipur')
        
