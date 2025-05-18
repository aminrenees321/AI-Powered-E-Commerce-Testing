import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.mobile
class TestMobileApp:
    def test_mobile_login(self, mobile_driver):
        username = mobile_driver.find_element(MobileBy.ID, "username")
        password = mobile_driver.find_element(MobileBy.ID, "password")
        login_btn = mobile_driver.find_element(MobileBy.ID, "login-btn")
        
        username.send_keys("mobile_user")
        password.send_keys("mobile_pass")
        login_btn.click()
        
        WebDriverWait(mobile_driver, 10).until(
            EC.presence_of_element_located((MobileBy.ID, "home-screen"))
        )
    
    def test_add_to_cart(self, mobile_driver):
        # Assuming we're already logged in
        product = mobile_driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='Add to Cart']")
        product.click()
        
        cart_badge = WebDriverWait(mobile_driver, 10).until(
            EC.presence_of_element_located((MobileBy.ID, "cart-badge"))
        )
        assert cart_badge.text == "1"