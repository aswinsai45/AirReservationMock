import mysql.connector as connector
import datetime, time


def timeformatter(date):
    d = datetime.datetime.strftime(date, "%Y-%m-%d")
    return d

username = 'AdminBreeze'
password = 'Admin000'

userin = input('Enter username: ')
passin = input('Enter password: ')

if not (userin == username and passin == password):
    print('Username/Password incorrect for Admin')
    exit()

con = connector.connect(host='localhost', user='root', passwd='mySQL1234$s-10763', database='tickets')
cur = con.cursor(buffered=True)



while True:
    print()
    print(
        '\n1. Retrieve All Reservations\n2. Cancel a Reservation\n3. Search for a Reservation\n4. Clear All Reservations\n5. Exit Admin Mode')
    print()

    ch = int(input('Enter your choice:'))
    if ch == 1:
        cur.execute('SELECT * FROM JOURNEYDETAILS;')
        v = cur.fetchall()
        if v:
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
        else:
            print('No Active Bookings till now.')

    elif ch == 2:
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
            print('Cancelling ticket..')
            time.sleep(3)
            print('Successfully Cancelled Ticket')

    elif ch == 3:
        sr = input('Enter Boarding Pass to Search: ')
        cur.execute('SELECT * FROM JOURNEYDETAILS WHERE boardingpass = "{}"'.format(sr))
        v = cur.fetchall()
        time.sleep(3)
        print('ALL RESERVATIONS UNDER ', sr)
        if v:
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
        else:
            print('No Active Bookings till now.')

    elif ch == 4:
        print('This action cannot be undone. ')
        conf = input('DELETE ALL RESERVATIONS? [Y/N]: ')
        if conf == 'Y' or conf == 'y':
            time.sleep(5)
            print('Deleting..')
            cur.execute('DELETE FROM JOURNEYDETAILS;')
            con.commit()
            print('DELETED ALL BOOKINGS')
        elif conf == 'N' or conf == 'n':
            print('Exiting menu')
            break
        else:
            print('Invalid input')
    elif ch == 5:
        print('Exiting Admin Mode')
        break
    else:
        print('Incorrect Input.. Exiting')
        break

