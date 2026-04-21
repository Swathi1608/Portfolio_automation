import os
import time

import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("launch_website")
class TestSetup:
    def locate_web_element(self, web_element):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(web_element))