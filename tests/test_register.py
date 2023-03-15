import pytest
from tests.test_basic import BasicTest


@pytest.mark.usefixtures("view_objects_creation")
class TestRegister(BasicTest):

    @pytest.mark.id1
    def test_register_user(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_new_user_name("Marian")
        self.login_page.input_new_user_email("brustyn123@gmail.com")
        self.login_page.click_signup_button()
        self.register_page.click_mr_radio_button()
        self.register_page.input_password("Bartek123")
        self.register_page.select_day_of_birth('5')
        self.register_page.select_month_of_birth('June')
        self.register_page.select_year_of_birth('1995')
        self.register_page.click_newsletter_checkbox()
        self.register_page.click_special_offer_checkbox()
        self.register_page.input_first_name("Bartosz")
        self.register_page.input_last_name("Rustyn")
        self.register_page.input_company_name("SII")
        self.register_page.input_address_1("Podgrodzie")
        self.register_page.input_address_2("Latoszyn")
        self.register_page.select_country("Australia")
        self.register_page.input_state("malopolska")
        self.register_page.input_city("Sydney")
        self.register_page.input_zipcode(123)
        self.register_page.input_mobile_number(765123908)
        self.register_page.click_create_button()
        assert self.register_page.is_account_created_text_is_visible()

    @pytest.mark.id5
    def test_register_user_with_existing_email(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_new_user_name("Bartosz")
        self.login_page.input_new_user_email("brustyn123@gmail.com")
        self.login_page.click_signup_button()
        assert self.login_page.is_alert_email_exist_displayed()


    

    

    
        
        
        

