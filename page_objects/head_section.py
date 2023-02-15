from selenium.webdriver.common.by import By


class HeadSection:

    signup_login_button = "a[href='/login']"




    def __init__(self, driver):
        self.driver = driver

    def click_signup_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, HeadSection.signup_login_button).click()

    