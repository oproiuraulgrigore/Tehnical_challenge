
from playwright.sync_api import expect
from methods.screenshot_help import take_screenshot


# Happy flow scenario for contact form

def test_contact_form(browser):
    page = browser.new_page()
    page.goto("https://automationintesting.online/")
    page.fill("#name" , "Raul Oproiu")
    page.fill("#email" , "oproiuraul4@gmail.com")
    page.fill("#phone" , "07411111111")
    page.fill("#subject", "Booking")
    page.fill("#description" , "Nothing to say for this booking")
    page.get_by_role("button", name="Submit").click()
    success_msg = page.get_by_text("Thanks for getting in touch")

    expect(success_msg).to_be_visible(timeout=10000)

    take_screenshot(page, "contact_form_success")

# Negative flow scenario for contact form - empty fields

def test_contact_form_negative(browser):
    page = browser.new_page()
    page.goto("https://automationintesting.online/")

    page.get_by_role("button", name="Submit").click()

    validation_messages = [
    "Name may not be blank",
    "Email may not be blank",
    "Phone may not be blank",
    "Phone must be between 11 and 21 characters.",
    "Subject may not be blank",
    "Subject must be between 5 and 100 characters.",
    "Message may not be blank",
    "Message must be between 20 and 2000 characters."
]
    for msg in validation_messages:
      expect(page.get_by_text(msg)).to_be_visible(timeout=5000)

    take_screenshot(page, "contact_form_empty_fields")