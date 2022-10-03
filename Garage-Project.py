import random
import os

class ParkingGarage():
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9]
        self.takenSpaces = {}
        self.currentTicket = {}
        self.rate = 5.0
        self.paid = False

    def takeTicket(self):
        os.system('cls')
        print('Welcome to the CartBo Parking Lot.')
        if len(self.parkingSpaces) == 0:
            print('I am sorry, the parking lot is full. There are no spaces left at the moment. Please come again another time.')
        else:
            print('Please take a ticket.')
            takenSpace = self.parkingSpaces.pop(0)               # pops out a space number from the parkingSpaces list and puts it into takenSpaces
            ticket_number = self.tickets.pop(0)                    # pops out a ticket number from self.tickets list.
            self.takenSpaces[ticket_number] = takenSpace           # self.takenSpaces is a dictionary with the ticket_number as the key and the space number (takenSpace) as the value
            self.currentTicket[ticket_number] = self.paid          # self.currentTicket is a dictionary with the ticket_number as the key and True/False Boolean (self.paid) as the value
            print(f'Your rate is $5 an hour.\nPlease park in space {takenSpace}.')

    def payForParking(self):
        os.system('cls')
        pay = input('Would you like to pay for your parking? \'y\' or \'n\'\n')
        if pay == 'y':
            ticket_number = input('What is your ticket number?\n')
            print('How long have you been parked with us?')                               # Rather than have a user input the
            parking_time = round(random.uniform(0.00, 12.00), 2)                          # time, it is randomly generated
            print(parking_time)
            if parking_time < 0.25:
                print("You have been here for less than 15 minutes, you do not have to pay. Thank you for choosing CartBo Parking.")
            else:
                print(f'You parked for {"{:.2f}".format(parking_time)} hours. Your cost to park is ${"{:.2f}".format(parking_time * self.rate)}.')
                insert_cc = input('To pay, please insert your credit card.\n(hit "Enter" when your credit card is entered)')
                if insert_cc == '':
                    self.currentTicket[int(ticket_number)] = True                         # Self.paid changed to True. 
                    print("Thank you for paying, you have 15 minutes to leave.")
        elif pay == 'n':
            print('Please come back when you\'re ready to pay.')
        else:
            print('Please type \'y\' or \'n\'')

    def leaveGarage(self):
        os.system('cls')
        ticket_number = input('I need your ticket number before you can leave CartBo Parking.\nWhat is your ticket number?\n')
        print()
        if ticket_number not in str(range(0,1000000000)):
            input('The ticket number must be a number. Please hit "Enter" to continue.')
            pg.leaveGarage()
        else:
            if self.currentTicket[int(ticket_number)] == True:
                print('The gate is open. Thank you for parking with us and have a nice day.')
                self.parkingSpaces.append(self.takenSpaces[int(ticket_number)])               # Adding space back into parkingSpaces list.
                del self.takenSpaces[int(ticket_number)]
                del self.currentTicket[int(ticket_number)]
                if len(self.tickets) == 0:                                                    # Adding a new ticket number to the end of the tickets list
                    self.tickets.append(max(self.takenSpaces, key=self.takenSpaces.get) + 1)  # taking into account that if all spaces are full, the 
                else:                                                                         # self.tickets dictionary gets appended with the max key of
                    self.tickets.append(max(self.tickets) + 1)                                # self.takenSpaces
            elif self.currentTicket[int(ticket_number)] == False:
                pay_now = input('You have not paid for parking.\nType \'y\' to pay now or \'n\' to pay later.\n')
                if pay_now == 'y':
                    pg.payForParking()
                elif pay_now == 'n':
                    print('Please come back to pay when you are ready.')
                else:
                    print('Please type \'y\' or \'n\'')


### ----------------------------- Test Cases ----------------------------- ###

pg = ParkingGarage()
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")
pg.takeTicket()
wait = input("Press Enter to continue.")                  # Once you execute this last portion it will move onto payForParking

pg.payForParking()
wait = input("Press Enter to continue.")
pg.payForParking()
wait = input("Press Enter to continue.")
pg.payForParking()
wait = input("Press Enter to continue.")

pg.leaveGarage()
wait = input("Press Enter to continue.")
pg.leaveGarage()
wait = input("Press Enter to continue.")
pg.leaveGarage()