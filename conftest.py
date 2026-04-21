import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def launch_website(request):
    service_obj = Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://swathi1608.github.io/Portfolio/")
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.quit()
