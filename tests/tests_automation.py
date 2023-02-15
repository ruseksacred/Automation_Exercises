import pytest
from page_objects import head_section

@pytest.mark.usefixtures("setup")
class BasicTest:
    pass



        
class TestsAutomation(BasicTest):

    @pytest.fixture()
    def view_objects_creation(self):
        self.head_section = head_section.HeadSection(self.driver)

    def test_register_user(self, view_objects_creation):
        self.head_section.click_signup_login_button()
