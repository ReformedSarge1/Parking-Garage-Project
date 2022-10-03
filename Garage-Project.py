import random

class ParkingGarage():
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9]
        self.ticket_number = 9
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9]
        self.currentTicket = {}
        self.tix_space_paid = []
        self.rate = 5.0
        self.paid = False
         
        

    def takeTicket(self):
        while True:
            welcome = input('Welcome to the CartBo Parking Lot.\nWould you like to park? \'y\' or \'n\'\n')
            if welcome == 'y':
                if len(self.parkingSpaces) == 0:
                    print('I am sorry, the parking lot is full. There are no spaces left at the moment. Please come again another time.')
                else:
                    random_space = random.randint(1,9)
                    self.parkingSpaces.remove(random_space)
                    self.tickets.pop(0)
                    self.tix_space_paid.append(self.tickets[0])
                    self.tix_space_paid.append(self.paid)
                    self.currentTicket = {random_space:self.tix_space_paid}
                    print(f'Your rate is $5 an hour, Here is your ticket. Please park in space {random_space}.')
                    return
            elif welcome == 'n':
                print('Thanks for considering parking in our lot. Have a great day!')
                break
            else:
                print('Please type \'y\' or \'n\'')


    def payForParking(self,time,space):
        self.time = time
        self.space = space
        if self.time < 0.25: 
            print("You have been here for 15 minutes, you do not have to pay. Thank you for choosing CartBo Parking.")
        else:
            print(f'Your cost to park is ${"{:.2f}".format(self.time * self.rate)}.')
            space = input(f"Which space were you parked in?")
            self.tix_space_paid[1] = True           #Self.paid = True. 
            self.currentTicket = {space:self.tix_space_paid}
            self.parkingSpaces.append(int(space))      #adding space back into space list.
            self.ticket_number += 1
            self.tickets.append(self.ticket_number)


    def leaveGarage(self): 
        if self.currentTicket[self.space]:
            print("Thank you for paying, you have 15 minutes to leave.")




pg = ParkingGarage()
pg.takeTicket()
pg.payForParking(7.5)