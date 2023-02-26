from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class HeadSection:

    signup_login_button = "a[href='/login']"
    test_cases_button = "a[href='/test_cases']"
    contact_us_button = "a[href='/contact_us']"
    products_button = "a[href='/products']"
    cart_button = "a[href='/view_cart']"

    def __init__(self, driver):
        self.driver = driver

    def click_signup_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.signup_login_button).click()

    def click_test_cases_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.test_cases_button).click()

    def click_contact_us_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.contact_us_button).click()

    def click_products_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.products_button).click()

    def click_cart_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cart_button).click()

    def is_alert_present(self):
        try:
           alert = self.driver.switch_to_alert()
           alert.accept()
        except:
            print("No alert")

    


    