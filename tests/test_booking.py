

from playwright.sync_api import Page
from playwright.sync_api import expect
from methods.screenshot_help import take_screenshot

# Happy flow scenario for booking form


def test_booking_form(page: Page):
     page.goto("https://automationintesting.online/")
    
     page.locator("a.btn.btn-primary[href*='/reservation/1']").click(timeout=15000)


     page.wait_for_url("**/reservation/1*")

     reserve_now_button = page.locator("#doReservation")
     reserve_now_button.wait_for(state="visible", timeout=10000)
     reserve_now_button.click()

     first_name_input = page.locator("input[name='firstname']")
     first_name_input.wait_for(state="visible", timeout=15000)
     page.fill("input[name='firstname']", "Raul")
     page.fill("input[name='lastname']", "Oproiu")
     page.fill("input[name='email']", "oproiuraul4@gmail.com")
     page.fill("input[name='phone']", "07411111111")

     reserve_button = page.get_by_role("button", name="Reserve Now")
     reserve_button.click()

     error_banner = page.locator("text=Application error")
     if error_banner.is_visible():
       print("Client-side error detected!")

     take_screenshot(page, "booking_form_submission")


# Negative flow scenario for booking form


def test_booking_form_negative_flows(page: Page):

   
    negative_cases = [
        {"firstname": "", "lastname": "", "email": "", "phone": "", "label": "empty"},
        {"firstname": "Raul", "lastname": "", "email": "invalid", "phone": "123", "label": "partial"},
        {"firstname": "", "lastname": "Oproiu", "email": "oproiuraul4@gmail.com", "phone": "", "label": "missing"},
    ]

    for case in negative_cases:
     page.goto("https://automationintesting.online/")
        
        
     page.locator("a.btn.btn-primary[href*='/reservation/1']").click(timeout=15000)
     page.wait_for_url("**/reservation/1*")

       
     reserve_now_button = page.locator("#doReservation")
     reserve_now_button.wait_for(state="visible", timeout=10000)
     reserve_now_button.click()

      
     page.fill("input[name='firstname']", case["firstname"])
     page.fill("input[name='lastname']", case["lastname"])
     page.fill("input[name='email']", case["email"])
     page.fill("input[name='phone']", case["phone"])

      
     reserve_button = page.get_by_role("button", name="Reserve Now")
     reserve_button.click()

       
     error_banner = page.locator("text=Application error")
     if error_banner.is_visible(timeout=5000):
        print(f"Client-side error detected! {case['label']}!")

       
     take_screenshot(page, f"booking_negative_{case['label']}")

