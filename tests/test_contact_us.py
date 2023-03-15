import pytest
from tests.test_basic import BasicTest
from selenium.webdriver.common.alert import Alert

@pytest.mark.usefixtures("view_objects_creation")
class TestContactUs(BasicTest):

    @pytest.mark.id6
    def test_contact_us_form(self, view_objects_creation):
        self.head_section.click_contact_us_button()
        self.contact_us_page.input_name("Bartosz")
        self.contact_us_page.input_email("brustyn123@gmail.com")
        self.contact_us_page.input_subject("Reklamacja")
        self.contact_us_page.input_meassage("Towar niezgodny z zamówieniem")
        self.contact_us_page.add_file_to_message(fr"C:\Users\brustyn\Downloads\wydruk.pdf")
        self.contact_us_page.click_submit_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert self.contact_us_page.is_status_alert_success_displayed()

