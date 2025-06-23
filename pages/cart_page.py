from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.utility import Utility
import time

class Cart:

    def __init__(self, driver):
        self.driver = driver


    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR ,".icon.icon-cart-empty")
    
    def cart_heading(self):
        self.driver.find_element(By.CSS_SELECTOR ,".cart-notification__heading.caption-large.text-body")
    
    
    def cart_product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR ,".cart-notification-product__name.h4")

    
    def verify_cart_name(self):
        self.driver.find_element(By.CSS_SELECTOR ,"#cart-notification-form")
    
    def cart_checkout(self):
        self.driver.find_element(By.XPATH ,"//button[@id='checkout']").click()
        time.sleep(3)

    def verify_label(self):
        self.driver.find_element(By.CSS_SELECTOR ,"button[class='link button-label']")

    def view_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#cart-notification-button").click()
        time.sleep(3)

    def verify_product_name(self):
        test_data = Utility.read_data_file('product_data')
        data=test_data[0]
        element= self.cart_product_name()
        text =element.text 
        assert text == data["product"]["name"]

    


    