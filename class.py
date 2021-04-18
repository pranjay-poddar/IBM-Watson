class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passanger = []

    def add_passangers(self,name):
        if not self.open_seats():
            return False
        else:
            self.passanger.append(name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passanger)

flight = Flight(2)
people = ["Rohan","Ron","John","Jay","Sia"]
for person in people:
    if flight.add_passangers(person):
        print(f"{person} is tested COVID negative")
    else:
        print(f"{person} is tested COVID positive")
