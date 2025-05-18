import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
class TestLogin:
    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.login("standard_user", "secret_sauce")
        assert "dashboard" in browser.current_url
    
    def test_invalid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.login("invalid_user", "wrong_password")
        assert "Invalid credentials" in login_page.get_error_message()