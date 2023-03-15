from selenium.webdriver.common.by import By

class ContactUsPage:

    name_field = "//input[@data-qa='name']"
    email_field = "//input[@data-qa='email']"
    subject_field = "//input[@data-qa='subject']"
    message_field = "//textarea[@data-qa='message']"
    submit_button = "//input[@data-qa='submit-button']"
    choose_file_button = "//input[@name='upload_file']"


    def __init__(self, driver):
        self.driver = driver

    def input_name(self, name):
        self.driver.find_element(By.XPATH, self.name_field).clear()
        self.driver.find_element(By.XPATH, self.name_field).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(By.XPATH, self.email_field).clear()
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def input_subject(self, subject):
        self.driver.find_element(By.XPATH, self.subject_field).clear()
        self.driver.find_element(By.XPATH, self.subject_field).send_keys(subject)

    def input_meassage(self, message):
        self.driver.find_element(By.XPATH, self.message_field).clear()
        self.driver.find_element(By.XPATH, self.message_field).send_keys(message)

    def add_file_to_message(self, file_path):
        self.driver.find_element(By.XPATH, self.choose_file_button).send_keys(file_path)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def is_status_alert_success_displayed(self):
       return self.driver.find_element(By.XPATH, "//div[@class='status alert alert-success']").is_displayed()

