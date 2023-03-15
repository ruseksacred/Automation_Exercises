import pytest
from tests.test_basic import BasicTest


@pytest.mark.usefixtures("view_objects_creation")
class TestLogin(BasicTest):

    @pytest.mark.id2
    def test_login_user_pass(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_login_email("brustyn123@gmail.com")
        self.login_page.input_login_password("Bartek123")
        self.login_page.click_login_button()
        assert self.login_page.is_logged_in_as_text_displayed()

    @pytest.mark.id3
    def test_login_user_fail(self, view_objects_creation):
        self.head_section.click_signup_login_button()
        self.login_page.input_login_email("brustyn@gmail.com")
        self.login_page.input_login_password("Bartek123")
        self.login_page.click_login_button()
        assert self.login_page.is_wrong_email_or_password_text_displayed()

    @pytest.mark.id4
    @pytest.mark.usefixtures("login_user")
    def test_logout_user(self, view_objects_creation):
        self.head_section.click_logout_button()
        assert self.driver.current_url == "https://automationexercise.com/login"


    