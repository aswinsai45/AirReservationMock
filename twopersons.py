import datetime
import random
import mysql.connector
import time


def progress(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes * '*', blanks * ' ', ']', f' {percent:.0f}%', sep='', end='', flush=True)



def valid1(x):
    timeValidator = datetime.date.today()
    if x > timeValidator:
        return True
    else:
        print('Cannot choose ', x, 'Please enter date correctly')  # Travel, PassportExp


def valid2(x):
    timeValidator = datetime.date.today()
    if x < timeValidator:
        return True  # DOB
    else:
        print('Cannot choose ', x, 'Please enter date correctly')  # dob


# Random integer boardGenerator for Boarding Pass
boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

# Passenger 1
print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter Passenger 1's name: ")
while True:
    DOB = (input("Enter Passenger 1's Date of Birth in yyyy-mm-dd format: "))
    validDOB = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
    if valid2(validDOB) == True:
        break

# Passenger 2
print("PASSENGER 2: ")

passenger2 = input("\nEnter Passenger 2's name: ")
while True:
    DOB2 = (input("Enter Passenger 2's Date of Birth in yyyy-mm-dd format: "))
    validDOB = datetime.datetime.strptime(DOB2, "%Y-%m-%d").date()
    if valid2(validDOB):
        break

while True:
    travelDate = (input("Enter departure date in yyyy-mm-dd format "))
    travelValidation = datetime.datetime.strptime(travelDate, "%Y-%m-%d").date()

    if valid1(travelValidation):
        break

# Departure and Arrival
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19. We suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below\n")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: ")

print("Now Enter your Destination Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")

# If travelling to a different county, passport is needed

departure =  departureCity + ', ' +departureCountry
destination = destinationCity + ', ' +destinationCountry


passport1 = ''
passport2 = ''
k = 0
if str(departureCountry) != str(destinationCountry):
    k = 1
    passport1 = input("Enter Passenger 1's Passport Number: ")
    while True:
        passportExp1 = (input("Enter expiration date of passport [in yyyy-mm-dd format]: "))
        passportExpValidation = datetime.datetime.strptime(passportExp1, "%Y-%m-%d").date()
        if valid1(passportExpValidation) and (passportExpValidation > travelValidation):
            break
        elif passportExpValidation < travelValidation:
            print('Passport Invalid for Travel')

    passport2 = input("Enter Passenger 2's Passport Number: ")
    while True:
        passportExp2 = (input("Enter expiration date of passport in yyyy-mm-dd format: "))
        passportExpValidation = datetime.datetime.strptime(passportExp2, "%Y-%m-%d").date()
        if valid1(passportExpValidation) and (passportExpValidation > travelValidation):
            break
        elif passportExpValidation < travelValidation:
            print('Passport Invalid for Travel, as of required travel date')
if k == 0:
    passport1 = passport2 = 'DOMESTIC TRAVEL'

import airline_Timing

import payment

print('Breezing through our servers and finalizing!')
print('This will take a moment\n Get Ready to Fly!')
for i in range(101):
    progress(i)
    time.sleep(0.1)

print()

print('Enjoy your flight!')

boardpass = "AX" + str(boardGen)
flnum = airline_Timing.pr + str(flightGen)

con = mysql.connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
cur = con.cursor()

cur.execute(
    'insert into journeydetails values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(passenger1, DOB, boardpass,
                                                                                        passport1,departure,destination,
                                                                                        airline_Timing.chosen,
                                                                                        airline_Timing.listTime,
                                                                                        travelDate,
                                                                                        flnum))

cur.execute(
    'insert into journeydetails values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(passenger2, DOB2, boardpass,
                                                                                        passport2,departure,destination,
                                                                                        airline_Timing.chosen,
                                                                                        airline_Timing.listTime,
                                                                                        travelDate,
                                                                                        flnum))
cur.execute('insert into BPass values("{}")'.format(boardpass))
con.commit()

print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS ", str(boardpass), "~~~")
