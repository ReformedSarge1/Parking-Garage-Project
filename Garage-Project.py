import random

class ParkingGarage():
    def __init__(self):#, toPay, ticket, space):
        self.tickets = [1,2,3,4,5,6,7,8,9]
        self.ticket_number = 9
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9]
        self.currentTicket = {}
        self.tix_space_paid = []
        # self.toPay = toPay
        # self.ticket = ticket
        # self.space = space

    def takeTicket(self):
        while True:
            welcome = input('Welcome to the CartBo Parking Lot.\nWould you like to park? \'y\' or \'n\'\n')
            if welcome == 'y':
                if len(self.parkingSpaces) == 0:
                    print('I am sorry, the parking lot is full. There are no spaces left at the moment. Please come again another time.')
                else:
                    random_space = random.randint(1,9)
                    self.parkingSpaces.remove(random_space)
                    self.tix_space_paid.append(self.tickets[0])
                    self.tix_space_paid.append(False)
                    self.currentTicket = {random_space:self.tix_space_paid}
                    print(f'Here is your ticket. Please park in space {random_space}.')
                    print(self.currentTicket)
                    return
            elif welcome == 'n':
                print('Thanks for considering parking in our lot. Have a great day!')
                break
            else:
                print('Please type \'y\' or \'n\'')


    def payForParking(self):
        self.toPay = input("How much you pay")

    # def leaveGarage(self):

pg = ParkingGarage()
pg.takeTicket()