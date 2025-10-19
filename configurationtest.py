import pytest
from playwright.sync_api import sync_playwright

# Path to Brave browser executable

BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            executable_path=BRAVE_PATH,
            args=["--no-sandbox"]
        )
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

