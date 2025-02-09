import datetime
import random
import mysql.connector
import time

# Function to validate future dates (Travel Date, Passport Expiry)
def is_future_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if date > datetime.date.today():
            return date
        print("Invalid date! Please enter a future date.")
    except ValueError:
        print("Invalid format! Use YYYY-MM-DD.")
    return None

# Function to validate past dates (DOB)
def is_past_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if date < datetime.date.today():
            return date
        print("Invalid date! Please enter a past date.")
    except ValueError:
        print("Invalid format! Use YYYY-MM-DD.")
    return None

# Function to get valid user input for a date
def get_valid_date(prompt, validation_func):
    while True:
        date = validation_func(input(prompt))
        if date:
            return date

# Generate boarding pass and flight number
boardGen = random.randint(28514, 68741)
flightGen = random.randint(22523, 92527)
boardpass = "AX" + str(boardGen)

# Travel Details
travel_date = get_valid_date("Enter departure date (YYYY-MM-DD): ", is_future_date)

print("\nNow Enter your Departure Location:")
departure_country = input("Departing Country: ")
departure_city = input("Departing City: ")
departure = f"{departure_city}, {departure_country}"

print("\nNow Enter your Destination Location:")
destination_country = input("Destination Country: ")
destination_city = input("Destination City: ")
destination = f"{destination_city}, {destination_country}"

international_travel = departure_country != destination_country

# Select airline
import airline_Timing
pr, chosen, listTime = airline_Timing.choose_airline()  # Correct way to call the function

# Collect number of passengers
while True:
    try:
        num_passengers = int(input("Enter number of passengers (1-3): "))
        if 1 <= num_passengers <= 3:
            break
        print("Invalid input! Enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input! Enter a valid number.")

# Storing passenger details in separate lists
names = []
dobs = []
passports = []
passport_expiries = []

for i in range(1, num_passengers + 1):
    print(f"\nPASSENGER {i} DETAILS:")
    names.append(input(f"Enter Passenger {i}'s name: "))
    dobs.append(get_valid_date(f"Enter Passenger {i}'s DOB (YYYY-MM-DD): ", is_past_date))

    if international_travel:
        passports.append(input(f"Enter Passenger {i}'s Passport Number: "))
        passport_expiries.append(get_valid_date(f"Enter Passport Expiry Date (YYYY-MM-DD): ", is_future_date))
    else:
        passports.append("DOMESTIC TRAVEL")
        passport_expiries.append(None)

# Payment processing
import payment

print("\nProcessing your booking...")
for i in range(101):
    print(f"\rProgress: [{'*' * (i // 5)}{' ' * (20 - i // 5)}] {i}%", end='', flush=True)
    time.sleep(0.05)
print("\nBooking Complete!")

# Save details to MySQL database
con = mysql.connector.connect(user='root', host='localhost', password='aswin000', database='tickets')
cur = con.cursor()

for i in range(num_passengers):
    cur.execute(
        "INSERT INTO journeydetails (Name, DOB, BoardingPass, Passport, Departure, Destination, Airline, DepartureTime, DepartureDate, FlightNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (names[i], dobs[i], boardpass, passports[i], departure, destination, chosen, listTime, travel_date, pr + str(flightGen))
    )

con.commit()

print(f"\n~~~ YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY! YOUR BOARDING PASS NUMBER IS {boardpass} ~~~")
