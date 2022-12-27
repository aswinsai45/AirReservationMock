import datetime
import random

price = random.randint(20000, 50000)

print('\nYour ticket price will be: ₹', price)

print('Now, please pay with your Debit/Credit Card here')

nameOnCard = input('\nName on Card: ')

while True:
    card_number = str(input('16- Digit Credit/Debit card number: '))
    cardLength = len(card_number)
    if cardLength == 16:
        break
    else:
        print('Invalid Number, try again: ')

while True:
    cardExp = input('Enter expiry date [yyyy-mm-dd]:')
    cardValidation = datetime.datetime.strptime(cardExp, "%Y-%m-%d").date()
    if cardValidation > datetime.date.today():
        break
    elif cardValidation == datetime.date.today():
        print("Don't forget to renew your card!")
        break
    else:
        print("Cannot choose a date in the past, -", cardExp + '\n')
        print("Try again")

while True:
    cvvCard = str(input("Enter 3 digit card's CVV: "))
    if len(cvvCard) == 3:
        break


print('Paid by: ', nameOnCard, ' | ', 'Transaction Approved for ', ('₹' + str(price)), ' | ', 'Card Number: XXXXXXXXXXXX', card_number[-1:-4])


