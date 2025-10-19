# Testing project 

- this project contains automated tests for UI / API functionalities for the following websites :
 
    https://automationintesting.online/ - UI 
    https://restful-booker.herokuapp.com/ - API 

 # Project instllation 

 1. Clone the repository : 

    git clone < https://github.com/oproiuraulgrigore/Tehnical_challenge.git >
    cd Tehnical_challenge

 2. Environment configuration :

    - create a virtual enviroment : 

      python3 -m venv venv
      source venv/bin/activate (for Mac / Linux)

 3. Install dependencies :
  
    pip install -r requirements.txt 

 4. Intall Playwright browsers : 

    playwright install

# Tests

UI Tests ( happy flows & negative flows ):

pytest tests/ --headed 

Covered scenarios : 

 - booking form : 
 Happy flow : successfully submit a booking form.
 Negative flow : detect application errors when input is invalid.
 - login
 Happy flow : Login attempt.
 Negative flow : Invalid credentials validation. 
 - contact form 
 Happy flow : Submit form successfully.
 Negative flow : Missing required fields or invalid input.


API Tests : 

pytest api_tests/tests/test_booking_api.py

Covered : 

 - GET /booking → Verify status 200 and returns a list of bookings.
 - POST /booking → Create a booking and verify bookingid in the response.
 - GET /booking/{id} → Verify the details of the created booking.


Future scenarios :
- more negative flows (invalid email , phone number format) 
- cross browser testing (Firefox - Safari)
- DELETE / PUT booking id
- data validation tests ( required fields)
- performance tests for API response

General improvements for the project : 
- integrate tests with CI/CD pipeline ( GitHub Actions)
- create multiple env ( staging / prod )


