# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.card_link = (By.XPATH, "(//a[@id='CardLink-template--24642132640046__product-grid-9841472176430'])[1]")

    def get_title(self):
        return self.driver.title
    
    def click_catalog(self):
         self.driver.find_element(By.CSS_SELECTOR, "#HeaderMenu-catalog").click()

    def click_card_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_link)
        )
        assert element.is_displayed(), "Card link should be visible"
        element.click()
