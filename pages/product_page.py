# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.utility import Utility
import time


class Product:

    def __init__(self, driver):
        self.driver = driver
        self.card_link = (
            By.XPATH,
            "(//a[@id='CardLink-template--24642132640046__product-grid-9841472176430'])[1]",
        )

    def store_heading(self):
        return self.driver.find_element(
            By.XPATH,
            "//p[@class='product__text inline-richtext caption-with-letter-spacing']",
        )

    def product_price(self):
        return self.driver.find_element(
            By.XPATH, "//span[@class='price-item price-item--regular']"
        )

    def product_title(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "div[class='product__title'] h1"
        )

    def add_product(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[name='plus']")

    def minus_product(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[name='minus']")

    def product_quantity(self):
        return self.driver.find_element(
            By.XPATH, "(//input[@id='Quantity-template--24642132836654__main'])[1]"
        )

    def add_cart(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "#ProductSubmitButton-template--24642132836654__main"
        )

    def add_buy(self):
        return self.driver.find_element(
            By.XPATH, "//button[normalize-space()='Buy it now']"
        )

    def get_text_from_element(self, element):
        text = element.text
        print(text)
        return text

    def verify_product_data(self, key):
        test_data = Utility.read_data_file('product_data')  # list of dicts

        for data in test_data:
            if key in data:
                if key == "store":
                    actual = self.get_text_from_element(self.store_heading())
                    expected = data[key]["name"]
                    assert (
                        actual == expected
                    ), f"Store heading mismatch: Expected '{expected}', Got '{actual}'"

                if key == "product":
                    assert (
                        self.get_text_from_element(self.product_title())
                        == data[key]["name"]
                    )
                    assert (
                        self.get_text_from_element(self.product_price())
                        == data[key]["price"]
                    )

                if key == "buttons":
                    assert (
                        self.get_text_from_element(self.add_cart())
                        == data[key]["add_to_cart"]
                    )
                    assert (
                        self.get_text_from_element(self.add_buy())
                        == data[key]["buy_it_now"]
                    )

    def click_on_add_cart(self):
        self.add_cart().click()
        time.sleep(3)
