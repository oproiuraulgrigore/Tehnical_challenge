

from playwright.sync_api import Page, expect
from methods.screenshot_help import take_screenshot

# Happy flow scenario for login as guest 


def test_login_as_guest(page: Page):

 page.goto("https://automationintesting.online/")
 page.get_by_role("link", name="Admin", exact=True).click()

 page.fill("#username", "Rauloproiu")
 page.fill("#password", "wrongpassword")

 page.locator("button", has_text="Login").click()
 expect(page.locator("text=Invalid credentials")).to_be_visible(timeout=5000)

 take_screenshot(page, "login_as_guest")


# Negative flow scenario for login 

def test_login_negative_flows(page: Page):
   
 test_cases = [
    {"username": "", "password": "", "label": "empty_fields"},
    {"username": "Rauloproiu", "password": "", "label": "missing_password"},
    {"username": "", "password": "wrongpassword", "label": "missing_username"},
    {"username": "Wronguser", "password": "wrongpassword", "label": "invalid_credentials"},
    ]
 
 for case in test_cases:
  page.goto("https://automationintesting.online/")
  page.get_by_role("link", name="Admin", exact=True).click()
  page.wait_for_url("**/admin")

 
  page.fill("#username", case["username"])
  page.fill("#password", case["password"])
       
  page.locator("button", has_text="Login").click()
     
  expect(page.locator("text=Invalid credentials")).to_be_visible(timeout=5000)
        
  take_screenshot(page, case["label"])

  page.goto("https://automationintesting.online/")

 

