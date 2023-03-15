from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class LoginPage:

    new_user_name_field = "//input[@type='text']"
    new_user_email_field = "//input[@data-qa='signup-email']"
    login_user_email_field = "//input[@data-qa='login-email']"
    login_password_field = "//input[@data-qa='login-password']"
    password_field = "//input[@data-qa='login-password']"
    signup_button = "//button[@data-qa='signup-button']"
    login_button = "//button[@data-qa='login-button']"
    
    
    def __init__(self, driver):
        self.driver = driver
        
    def input_new_user_name(self, user_name):
        self.driver.find_element(By.XPATH, self.new_user_email_field).clear()
        self.driver.find_element(By.XPATH, self.new_user_name_field).send_keys(user_name)

    def input_new_user_email(self, user_email):
        self.driver.find_element(By.XPATH, self.new_user_email_field).clear()
        self.driver.find_element(By.XPATH, self.new_user_email_field).send_keys(user_email)

    def input_login_email(self, email):
        self.driver.find_element(By.XPATH, self.login_user_email_field).clear()
        self.driver.find_element(By.XPATH, self.login_user_email_field).send_keys(email)

    def input_login_password(self, password):
        self.driver.find_element(By.XPATH, self.login_password_field).clear()
        self.driver.find_element(By.XPATH, self.login_password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()

    
    def is_wrong_email_or_password_text_displayed(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']").is_displayed()
    
    def is_logged_in_as_text_displayed(self):
        return self.driver.find_element(By.XPATH, "//header[@id='header']//li[10]//a[1]//i[@class = 'fa fa-user']").is_displayed()
    
    def is_alert_email_exist_displayed(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='Email Address already exist!']").is_displayed()
        

    

    
    
    

    
      

