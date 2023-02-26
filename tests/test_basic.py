import pytest
from page_objects import head_section
from page_objects import login_page
from page_objects import register_page


@pytest.mark.usefixtures("setup")
class BasicTest:
    @pytest.fixture()
    def view_objects_creation(self):
        self.head_section = head_section.HeadSection(self.driver)
        self.login_page = login_page.LoginPage(self.driver)
        self.register_page = register_page.RegisterPage(self.driver)