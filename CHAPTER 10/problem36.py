#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
#and get fare information of train running under Indian Railways

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")
        
    def get_status(self):
        print(f"train {self.trainNo} is running on time")

    def get_fare(self, fro, to):
        print(f"The fare of Ticket booked in train no {self.trainNo} from {fro} to {to} is {randint(200,500)}")


t = Train(12239)
t.book("Raipur", "Pune")
t.get_status()
t.get_fare("Raipur", "Pune")