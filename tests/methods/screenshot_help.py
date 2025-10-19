import os
from datetime import datetime

def take_screenshot(page, label: str):
    
    # This method take a screenshot of the current page state and saves it.

    screenshots_dir = os.path.join("tests", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(screenshots_dir, f"{label}_{timestamp}.png")
    page.screenshot(path=path, full_page=True)
    print(f"📸 Screenshot salvat: {path}")
    return path
