# tests/test_homepage.py
import time

def test_homepage_title(home_page,product_page,cart_page,checkout_page):
    time.sleep(2)  # Optional; use WebDriverWait in real tests
    assert "Best Store" in home_page.get_title()
    home_page.click_catalog()
    home_page.click_card_link()
    product_page.verify_product_data("store")
    product_page.verify_product_data("product")
    product_page.verify_product_data("buttons")
    product_page.click_on_add_cart()

    cart_page.verify_product_name()
    cart_page.view_cart()
    cart_page.cart_checkout()

    checkout_page.email_address()
    checkout_page.select_country()

    


