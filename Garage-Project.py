class ParkingGarage():
    def __init__(self, toPay):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}
        self.toPay = toPay

    def taketicket(self):
        for ticket in self.tickets:
            ticket -= 1
            self.parkingSpaces -= 1
    def payforparking(self):
        self.toPay = input("How much you pay")

    def leavegarage(self):

    