import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
