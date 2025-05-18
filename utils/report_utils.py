import allure
import os

def attach_screenshot(browser, name):
    screenshot_path = os.path.join("reports", "screenshots", f"{name}.png")
    browser.save_screenshot(screenshot_path)
    allure.attach.file(
        screenshot_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

def attach_response_data(response):
    allure.attach(
        str(response.json()),
        name="API Response",
        attachment_type=allure.attachment_type.JSON
    )