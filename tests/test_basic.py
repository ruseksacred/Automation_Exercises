import pytest
from page_objects import head_section
from page_objects import login_page
from page_objects import register_page
from page_objects import contact_us_page


@pytest.mark.usefixtures("setup")
class BasicTest:
    @pytest.fixture()
    def view_objects_creation(self):
        self.head_section = head_section.HeadSection(self.driver)
        self.login_page = login_page.LoginPage(self.driver)
        self.register_page = register_page.RegisterPage(self.driver)
        self.contact_us_page = contact_us_page.ContactUsPage(self.driver)

    @pytest.fixture()
    def login_user(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_login_email("brustyn123@gmail.com")
        self.login_page.input_login_password("Bartek123")
        self.login_page.click_login_button()