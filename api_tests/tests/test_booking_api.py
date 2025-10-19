import sys
import os
import pytest
import requests

# Project path (safe imports)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fixtures.api_client import api_client
from helpers.helpers import generate_booking_payload

BASE_URL = "https://restful-booker.herokuapp.com"


# 1 GET returns 200 ok and a list of bookings

@pytest.mark.api
def test_get_all_bookings(api_client):
   
    response = api_client.get(f"{BASE_URL}/booking")
    assert response.status_code == 200 
    assert isinstance(response.json(), list)


# 2 POST creates a new booking 

@pytest.mark.api
def test_create_booking(api_client):
   
    payload = generate_booking_payload()
    response = api_client.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200 
    data = response.json()
    assert "bookingid" in data 
    assert "booking" in data 

# 3 GET booking by ID returns correct details

@pytest.mark.api
def test_get_booking_by_id(api_client):
    
    payload = generate_booking_payload()
    create_response = api_client.post(f"{BASE_URL}/booking", json=payload)
    booking_id = create_response.json().get("bookingid")

    get_response = api_client.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 200 

    booking_data = get_response.json()
    assert booking_data["firstname"] == payload["firstname"]
    assert booking_data["lastname"] == payload["lastname"]


