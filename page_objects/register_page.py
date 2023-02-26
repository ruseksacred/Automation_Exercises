from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class RegisterPage:

    mr_radio_button = "id_gender1"
    mrs_radio_button = "id_gender2"
    days_dropdown = "days"
    months_dropdown = "months"
    years_dropdown = "years"
    newsletter_checkbox = "newsletter"
    special_offer_checkbox = "optin"
    first_name_field = "first_name"
    last_name_field = "last_name"
    company_field = "company"
    address_1_field = "address1"
    address_2_field = "address2"
    country_dropdown = "country"
    state_field = "state"
    city_field = "city"
    zipcode_field = "zipcode"
    mobile_number_field = "mobile_number"
    create_account_button = "//button[@data-qa ='create-account']"

    

    def __init__(self, driver):
        self.driver = driver

    
    def click_mr_radio_button(self):
        self.driver.find_element(By.ID, self.mr_radio_button).click()

    def click_mrs_radio_button(self):
        self.driver.find_element(By.ID, self.mrs_radio_button).click()

    def input_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).clear()
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def select_day_of_birth(self, day):
        select = Select(self.driver.find_element(By.ID, self.days_dropdown))
        select.select_by_value(day)

    def select_month_of_birth(self, month):
        select = Select(self.driver.find_element(By.ID, self.months_dropdown))
        select.select_by_visible_text(month)

    def select_year_of_birth(self, year):
        select = Select(self.driver.find_element(By.ID, self.years_dropdown))
        select.select_by_visible_text(year)

    def click_newsletter_checkbox(self):
        self.driver.find_element(By.ID, self.newsletter_checkbox).click()

    def click_special_offer_checkbox(self):
        self.driver.find_element(By.ID, self.special_offer_checkbox).click()

    def input_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field).clear()
        self.driver.find_element(By.ID, self.first_name_field).send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field).clear()
        self.driver.find_element(By.ID, self.last_name_field).send_keys(last_name)

    def input_company_name(self, company_name):
        self.driver.find_element(By.ID, self.company_field).clear()
        self.driver.find_element(By.ID, self.company_field).send_keys(company_name)

    def input_address_1(self, address):
        self.driver.find_element(By.ID, self.address_1_field).clear()
        self.driver.find_element(By.ID, self.address_1_field).send_keys(address)

    def input_address_2(self, address):
        self.driver.find_element(By.ID, self.address_2_field).clear()
        self.driver.find_element(By.ID, self.address_2_field).send_keys(address)

    def select_country(self, country):
        select = Select(self.driver.find_element(By.ID, self.country_dropdown))
        select.select_by_visible_text(country)

    def input_state(self, state):
        self.driver.find_element(By.ID, self.state_field).clear()
        self.driver.find_element(By.ID, self.state_field).send_keys(state)
        
    def input_city(self, city):
        self.driver.find_element(By.ID, self.city_field).clear()
        self.driver.find_element(By.ID, self.city_field).send_keys(city)

    def input_zipcode(self, zipcode):
        self.driver.find_element(By.ID, self.zipcode_field).clear()
        self.driver.find_element(By.ID, self.zipcode_field).send_keys(zipcode)

    def input_mobile_number(self, mobile_number):
        self.driver.find_element(By.ID, self.mobile_number_field).clear()
        self.driver.find_element(By.ID, self.mobile_number_field).send_keys(int(mobile_number))

    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.create_account_button).click()

    def is_account_created_text_is_visible(self):
        return self.driver.find_element(By.XPATH, "//b[text()='Account Created!']").is_displayed()

