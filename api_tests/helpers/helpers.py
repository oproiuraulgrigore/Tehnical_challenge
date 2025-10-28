
import random
import string

#Function to generate random booking payloads

def generate_booking_payload():
    
    firstname = ''.join(random.choices(string.ascii_letters))
    lastname = ''.join(random.choices(string.ascii_letters))
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": random.randint(10, 1000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-10-20",
            "checkout": "2025-10-30"
        },
        "additionalneeds": "breakfast & dinner"
    }

