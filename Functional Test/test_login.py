import action
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.support.expected_conditions import alert_is_present
import pytest
from pytest import fixture
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.login_page import LoginPage
from utility.test_setup import TestSetup


@pytest.mark.login_page_tests
class TestLoginPage(TestSetup):
#TC_LOGIN_001 — Verify login page loads with username field, password field, login button, and credentials box visible
    def test_portfolio_login_structure(self):
        login_page_labels = LoginPage(self.driver)
        text_1 = login_page_labels.get_logo_label().is_displayed()
        assert text_1 == True, "Initials SR are not visible in the Logo"
        text_2 = login_page_labels.get_logo_h1_label().is_displayed()
        assert text_2 == True, "Heading Swathi R | QA Portfolio not visible in the Logo"
        text_3 = login_page_labels.get_logo_para_label().is_displayed()
        assert text_3 == True, "One line Paragraph Quality Assurance Engineer not visible in the Logo"
        text_4 = login_page_labels.get_username_label().is_displayed()
        assert text_4 == True, "USERNAME label is not visible in the Login Page"
        text_5 = login_page_labels.get_password_label().is_displayed()
        assert text_5 == True, "PASSWORD label is not visible in the Login Page"
        text_6 = login_page_labels.get_login_label().is_displayed()
        assert text_6 == True, "Login to Portfolio label is not visible in the Login Page"
        text_7 = login_page_labels.get_credential_label().is_displayed()
        assert text_7 == True, "Demo Credentials label is not visible in the Login Page"
        input_box_1 = login_page_labels.get_user_name().is_displayed(), "Username input box not visible in the Login Page"
        input_box_2 = login_page_labels.get_password_label().is_displayed(), "Password input box not visible in the Login Page"

#TC_LOGIN_002 — Verify login with valid credentials (swathi / qaportal123) navigates to portfolio page
    def test_valid_login(self):
        login_success = LoginPage(self.driver)
        login_success.get_user_name().send_keys("swathi")
        login_success.get_password().send_keys("qaportal123")
        login_success.get_login_button().click()
        login_success.get_log_out_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Are you sure you want to logout?"
        alert.accept()

#TC_LOGIN_003 — Verify login with invalid username shows alert with message "Invalid credentials. Please try again."
    def test_invalid_username_login(self):
        login_fail_1 = LoginPage(self.driver)
        login_fail_1.get_user_name().send_keys("swathiiiii")
        login_fail_1.get_password().send_keys("qaportal123")
        login_fail_1.get_login_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Invalid credentials. Please try again." in alert.text
        alert.accept()


#TC_LOGIN_004 — Verify login with invalid password shows alert with error message
    def test_invalid_password_login(self):
        login_fail_2 = LoginPage(self.driver)
        login_fail_2.get_user_name().send_keys("swathi")
        login_fail_2.get_password().send_keys("qaportal12345")
        login_fail_2.get_login_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Invalid credentials. Please try again." in alert.text
        alert.accept()

#TC_LOGIN_005 — Verify login with both fields empty shows alert
    def test_empty_fields_login(self):
        login_fail_3 = LoginPage(self.driver)
        login_fail_3.get_user_name().send_keys("")
        login_fail_3.get_password().send_keys("")
        login_fail_3.get_login_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Invalid credentials. Please try again." in alert.text
        alert.accept()

    #TC_LOGIN_006 — Verify login with valid username and empty password shows alert
    def test_empty_username_login(self):
        login_fail_4 = LoginPage(self.driver)
        login_fail_4.get_user_name().send_keys("swathi")
        login_fail_4.get_password().send_keys("")
        login_fail_4.get_login_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Invalid credentials. Please try again." in alert.text
        alert.accept()

#TC_LOGIN_007 — Verify login with empty username and valid password shows alert
    def test_empty__password_login(self):
        login_fail_5 = LoginPage(self.driver)
        login_fail_5.get_user_name().send_keys("")
        login_fail_5.get_password().send_keys("qaportal123")
        login_fail_5.get_login_button().click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Invalid credentials. Please try again." in alert.text
        alert.accept()

#TC_LOGIN_008 — Verify pressing Enter key with valid credentials navigates to portfolio page
    def test_valid_login_with_keyboard_enter(self):
         login_success_1 = LoginPage(self.driver)
         login_success_1.get_user_name().send_keys("swathi")
         login_success_1.get_password().send_keys("qaportal123")
         action = ActionChains(self.driver)
         action.send_keys(Keys.ENTER).perform()
         login_success_1.get_log_out_button().click()
         wait = WebDriverWait(self.driver, 10)
         alert = wait.until(EC.alert_is_present())
         assert alert.text == "Are you sure you want to logout?"
         alert.accept()

#TC_LOGIN_009 — Verify pressing Enter key with invalid credentials shows alert
    def test_invalid_login_with_keyboard_enter(self):
         login_fail_6 = LoginPage(self.driver)
         login_fail_6.get_user_name().send_keys("swathiiiii")
         login_fail_6.get_password().send_keys("qaportal123")
         action = ActionChains(self.driver)
         action.send_keys(Keys.ENTER).perform()
         wait = WebDriverWait(self.driver, 10)
         alert = wait.until(EC.alert_is_present())
         assert "Invalid credentials. Please try again." in alert.text
         alert.accept()

#TC_LOGIN_010 — Verify demo credentials box displays username as swathi and password as qaportal123
    def test_credential_box_data(self):
        cred_data = LoginPage(self.driver)
        text = cred_data.get_credential_box_data().text
        assert "swathi" in text, "Username not displayed correctly in credentials box"
        assert "qaportal123" in text, "Password not displayed correctly in credentials box"

#TC_LOGIN_011 — Verify password field masks input
    def test_password_mask(self):
        password_mask = LoginPage(self.driver)
        password_mask.get_password()
        field_type = password_mask.get_password().get_attribute("type")
        assert field_type == "password", f"Expected type 'password', but got '{field_type}'"



