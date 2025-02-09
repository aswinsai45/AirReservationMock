import datetime
import random

listofairlines = {
    1: 'Air India', 2: 'United Airlines', 3: 'Emirates', 4: 'Etihad Airways',
    5: 'Qatar Airways', 6: 'IndiGo', 7: 'SpiceJet', 8: 'Vistara Airlines'
}

airline_codes = {
    1: "AI", 2: "UA", 3: "EK", 4: "EY", 5: "QTR", 6: "6E", 7: "SG", 8: "UKV"
}

def choose_airline():
    """Function to choose an airline and flight time."""
    global pr, chosen, listTime  # These will be used in airReservation.py

    print('The available airlines are:\n', listofairlines)

    while True:
        try:
            airline = int(input("Enter airline Index: "))
            if airline in listofairlines:
                pr = airline_codes[airline]
                chosen = listofairlines[airline]
                print(f'You have chosen: {chosen}')
                break
            else:
                print("Airline Unavailable/Incorrect. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate 3 random flight times
    times = {i+1: f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:00" for i in range(3)}


    print('\nThe available flight times are:', times)
    
    while True:
        try:
            user_choice = int(input("Enter the index for your preferred time: "))
            if user_choice in times:
                listTime = times[user_choice]
                print(f'You have chosen {chosen} at {listTime}')
                break
            else:
                print('Invalid choice. Try again.')
        except ValueError:
            print("Invalid input. Please enter a number.")

    return pr, chosen, listTime  # Return values for use in airReservation.py
