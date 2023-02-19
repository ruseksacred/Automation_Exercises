import pytest
from page_objects import head_section
from page_objects import login_page

@pytest.mark.usefixtures("setup")
class BasicTest:
    pass

class TestsAutomation(BasicTest):

    @pytest.fixture()
    def view_objects_creation(self):
        self.head_section = head_section.HeadSection(self.driver)
        self.login_page = login_page.LoginPage(self.driver)

    def test_register_user(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_new_user_name("Marian")
        self.login_page.input_new_user_email("brustyn12345@gmail.com")
        self.login_page.click_signup_button()
        self.login_page.click_mr_radio_button()
        self.login_page.input_password("Bartek123")
        self.login_page.select_day_of_birth('5')
        self.login_page.select_month_of_birth('June')
        self.login_page.select_year_of_birth('1995')
        self.login_page.click_newsletter_checkbox()
        self.login_page.click_special_offer_checkbox()
        self.login_page.input_first_name("Bartosz")
        self.login_page.input_last_name("Rustyn")
        self.login_page.input_company_name("SII")
        self.login_page.input_address_1("Podgrodzie")
        self.login_page.input_address_2("Latoszyn")
        self.login_page.select_country("Australia")
        self.login_page.input_state("malopolska")
        self.login_page.input_city("Sydney")
        self.login_page.input_zipcode(123)
        self.login_page.input_mobile_number(765123908)
        self.login_page.click_create_button()
        assert self.login_page.is_account_created_text_is_visible()


