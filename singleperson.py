import datetime
import random
import time
import mysql.connector

timeValidator = datetime.date.today()


def progress(percent=10, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'*', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)



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
        print('Cannot choose ', x, 'Please enter date correctly')


boardGen = random.randint(2000, 9000)
flightGen = random.randint(22523, 92527)

print('ENTER YOUR DETAILS CAREFULLY')
passenger1 = input("\nEnter your name: ")


while True:
    DOB = (input("Enter your Date of Birth in yyyy-mm-dd format: "))
    validDOB = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
    if valid2(validDOB) == True:
        break

while True:
    travelDate = (input("Enter departure date in yyyy-mm-dd format "))
    travelValidation = datetime.datetime.strptime(travelDate, "%Y-%m-%d").date()

    if valid1(travelValidation) == True:
        break

# departure and destinations
print(
    '\n' + 'Departure/Arrival to limited countries due to Covid -19. We suggest checking with the guidelines of '
           'the place you are travelling to\n')

print("Now Enter your Departure Location below\n")
departureCountry = input("Departing Country?: ")
departureCity = input("Departing City?: ")

print("Now Enter your Destination Location below\n")
destinationCountry = input("Destination Country?: ")
destinationCity = input("Destination City?: ")


departure =  departureCity + ', ' +departureCountry
destination = destinationCity + ', ' +destinationCountry



k = 0
passportNumber = ''
if str(departureCountry) != str(destinationCountry):
    k = 1
    passportNumber = input("Enter your Passport Number: ")
    while True:
        passportExpiry = (input("Enter expiration date of passport in yyyy-mm-dd format: "))
        passportExpValidation = datetime.datetime.strptime(passportExpiry, "%Y-%m-%d").date()
        if valid1(passportExpValidation) and (passportExpValidation > travelValidation):
            break
        elif passportExpValidation < travelValidation:
            print('Passport Invalid for Travel, as of required travel date')


if k == 0:
    passportNumber = 'DOMESTIC TRAVEL'

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

con = mysql.connector.connect(user='root', host='localhost', password='aswin000', database='tickets')
cur = con.cursor()

cur.execute(
    'insert into journeydetails values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(passenger1, DOB, boardpass,
                                                                                        passportNumber, departure,destination,
                                                                                        airline_Timing.chosen,
                                                                                        airline_Timing.listTime,
                                                                                        travelDate,
                                                                                        flnum))

cur.execute('insert into BPass values("{}")'.format(boardpass))

con.commit()


print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS ", boardpass, "~~~")
