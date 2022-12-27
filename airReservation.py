import mysql.connector as connector
import datetime

print("\n\nBook Flights with Ease on BREEZE! How can we help you today?\n")


def timeformatter(date):
    d = datetime.datetime.strftime(date, "%Y-%m-%d")
    return d


action = {1: "Book a ticket", 2: "Retrieve a ticket", 3: "Cancel a ticket", 4: "ADMIN CONTROL", 5: "Exit"}

print(action)
userEnter = int(input("\nEnter the Index: "))
dictAccess = action[userEnter]
print(dictAccess)


# Books a Ticket

def bookticket():
    print('~~You have chose to book a ticket~~')
    ch = int(input("\nEnter the number of people travelling [up-to 3]: "))
    if ch == 1:
        import singleperson
    elif ch == 2:
        import twopersons
    elif ch == 3:
        import threepersons
    else:
        print("Sorry, unavailable as of now. Thanks for understanding!")
        exit()


def retrieveticket():
    print('~~You have chose to retrieve a ticket~~')
    boardingPass = input('Enter boarding pass number here: ')
    con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
    cur = con.cursor()
    cur.execute('Select * from journeydetails where boardingpass = "{}"'.format(boardingPass))
    v = cur.fetchall()

    for row in v:
        l = []
        for col in row:
            l.append(col)

        print('Name: ', l[0])
        date1 = l[1]
        print('Date of Birth: ', timeformatter(date1))
        print('Boarding Pass Number: ', l[2])
        print('Passport Number: ', l[3])
        print('Departure Location: ', l[4])
        print('Destination Location: ', l[5])
        print('Airline: ', l[6])
        print('Departure Time: ', l[7])
        date2 = l[8]
        print('DepartureDate: ', timeformatter(date2))
        print('Flight Number: ', l[9])
        print('\n\n')


def cancelticket():
    print("~~You have chose to cancel a ticket~~")
    boardingPassCancel = input('Please enter boarding pass number here: ')
    con = connector.connect(user='root', host='localhost', password='mySQL1234$s-10763', database='tickets')
    cur = con.cursor(buffered=True)
    cur.execute('select * from journeydetails where boardingpass = "{}"'.format(boardingPassCancel))
    v = cur.fetchall()
    if v == []:
        print('BoardingPass Incorrect/Not Found')

    else:
        cur.execute('delete from journeydetails where boardingpass = "{}"'.format(boardingPassCancel))
        con.commit()
        print('Successfully Cancelled Ticket :(')


if userEnter == 1:
    bookticket()

elif userEnter == 2:
    retrieveticket()

elif userEnter == 3:
    cancelticket()

elif userEnter == 4:
    import admin
elif userEnter == 5:
    print('Exiting..')
    exit()
else:
    print('Sorry command not available. Try Again')
    exit()
