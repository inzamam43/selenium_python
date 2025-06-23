import mailslurp_client
import pytest
import re
import mailslurp_client
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import Product
from pages.cart_page import Cart
from dotenv import load_dotenv
import os



@pytest.fixture
def home_page(browser):
    return HomePage(browser)


@pytest.fixture
def product_page(browser):
    return Product(browser)

@pytest.fixture
def cart_page(browser):
    return Cart(browser)




@pytest.fixture(scope="function")
def browser():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("base_url"))
    yield driver
    driver.quit()

@pytest.fixture
def sign_in(browser):
    load_dotenv()
    # Step 1: MailSlurp config
    configuration = mailslurp_client.Configuration()
    configuration.api_key['x-api-key'] = os.getenv("api_key")

    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox = inbox_controller.create_inbox()
        email_address = inbox.email_address
        inbox_id = inbox.id
        print(f"Generated test email: {email_address}")

        # Step 2: Navigate to registration and fill form
        browser.get(os.getenv("base_url"))  
        browser.find_element(By.XPATH ,"(//*[name()='svg'][@class='icon icon-account'])[2]").click()
        browser.find_element(By.CSS_SELECTOR, "#email").send_keys(email_address)
        # browser.find_element(By.ID, "username").send_keys("testuser123")
        # browser.find_element(By.ID, "password").send_keys("StrongPass123!")
        browser.find_element(By.CSS_SELECTOR, "button[name='commit']").click()

        # Step 3: Wait for incoming email
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
        print("Waiting for verification email...")

        email = wait_for_controller.wait_for_latest_email(
            inbox_id=inbox_id,
            timeout=60000,
            unread_only=True
        )

        print(f"Email received: {email.subject}")

        # Step 4: Extract link from email
        match = re.search(r'https://[^\s]+', email.body)
        if match:
            verification_link = match.group(0)
            print(f"🔗 Verification link found: {verification_link}")
            browser.get(verification_link)
        else:
            raise Exception("No verification link found in email body.")

        yield email_address  # You can return email for later use if needed
