from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-btn")
    PRODUCT_CARD = (By.CLASS_NAME, "product-card")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    CART_ICON = (By.ID, "cart-icon")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def add_to_cart(self, product_index=0):
        products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARD))
        products[product_index].find_element(*self.ADD_TO_CART_BUTTON).click()
    
    def go_to_cart(self):
        self.click(self.CART_ICON)