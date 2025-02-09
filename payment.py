import datetime
import random

def validate_card_number():
    """Validates a 16-digit credit/debit card number."""
    while True:
        card_number = input("Enter 16-digit Credit/Debit Card number: ").strip()
        if card_number.isdigit() and len(card_number) == 16:
            return card_number
        print("Invalid card number! Please enter a valid 16-digit number.")

def validate_expiry_date():
    """Validates that the expiry date is in the future."""
    while True:
        try:
            card_exp = input("Enter card expiry date [YYYY-MM]: ").strip()
            exp_date = datetime.datetime.strptime(card_exp, "%Y-%m")
            if exp_date > datetime.datetime.today():
                return card_exp
            print("Card expiry date must be in the future!")
        except ValueError:
            print("Invalid format! Please enter in YYYY-MM format.")

def validate_cvv():
    """Validates a 3-digit CVV."""
    while True:
        cvv = input("Enter 3-digit CVV: ").strip()
        if cvv.isdigit() and len(cvv) == 3:
            return cvv
        print("Invalid CVV! Please enter a valid 3-digit CVV.")

# Generate a random ticket price
price = random.randint(20000, 50000)
print(f"\nYour ticket price is: ₹{price}")

# Payment details
print("\nPlease enter your Debit/Credit Card details:")
name_on_card = input("Name on Card: ").strip()
card_number = validate_card_number()
expiry_date = validate_expiry_date()
cvv = validate_cvv()

# Masked card display for security
masked_card = "XXXXXXXXXXXX" + card_number[-4:]

print("\nProcessing payment...")
print(f"Paid by: {name_on_card} | Transaction Approved for ₹{price} | Card Number: {masked_card}")

print("\nPayment Successful! 🎉")
