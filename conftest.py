import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appium import webdriver as appium_driver
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")  # Remove for visible browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def mobile_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": os.path.join(os.getcwd(), "app", "ecommerce-app.apk"),
        "automationName": "UiAutomator2"
    }
    driver = appium_driver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

@pytest.fixture
def api_client():
    base_url = os.getenv("API_BASE_URL", "https://api.mock-ecommerce.com")
    return base_url