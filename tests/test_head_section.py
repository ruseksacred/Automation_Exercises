import pytest
from tests.test_basic import BasicTest
from selenium.webdriver.common.alert import Alert


@pytest.mark.usefixtures("view_objects_creation")
class TestHeadSection(BasicTest):

    def test_contact_us_button(self, view_objects_creation):
        self.head_section.click_contact_us_button()
        self.head_section.is_alert_present()
        assert self.driver.current_url == "https://automationexercise.com/contact_us"

    @pytest.mark.id7
    def test_verify_test_case_page(self, view_objects_creation):
        self.head_section.click_test_cases_button()
        self.head_section.is_alert_present()
        assert self.driver.current_url == "https://automationexercise.com/test_cases"

    @pytest.mark.id8
    def test_product_button(self, view_objects_creation):
        self.head_section.click_products_button()
        self.head_section.is_alert_present()
        assert self.driver.current_url == "https://automationexercise.com/products"

    def test_cart_button(self, view_objects_creation):
        self.head_section.click_cart_button()
        self.head_section.is_alert_present()
        assert self.driver.current_url == "https://automationexercise.com/view_cart"
