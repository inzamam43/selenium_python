from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.utility import Utility
import time

class Checkout:

    def __init__(self, driver):
        self.driver = driver

    
    def email_address(self):
        select_element = self.driver.find_element(By.XPATH, "(//select[starts-with(@id, 'Select')])[1]")
        select_element.send_keys('abc@emai.com')
        
    
    def select_country(self):
        # XPath that matches any select with id starting with "Select"
        select_element = self.driver.find_element(By.XPATH, "(//select[starts-with(@id, 'Select')])[1]")

        select = Select(select_element) 
        country = self.driver.find_element(By.CSS_SELECTOR, 'option[value=PK]')
        select.select_by_visible_text('Pakistan')
        assert country.is_selected()
