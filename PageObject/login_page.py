from selenium.webdriver.common.by import By


class LoginPage:
    logo_label = (By.CLASS_NAME, "initials")
    logo_h1_label = (By.TAG_NAME, "h1")
    logo_para_label = (By.TAG_NAME, "p")
    username_label = (By.XPATH, "//label[text()='Username']")
    password_label = (By.XPATH,"//label[text()='Password']")
    login_label = (By.XPATH,"//button[text()='Login to Portfolio']")
    credential_label = (By.CLASS_NAME, "credentials-box")
    user_name = (By.ID, "usernameInput")
    password = (By.ID, "passwordInput")
    login_button = (By.XPATH, "//button[@class='btn-login']")
    credential_data = (By.CLASS_NAME, "credentials-box")
    logout_button = (By.XPATH, "//button[@class='btn-logout']")

    def __init__(self, driver):
        self.driver = driver

    def get_logo_label(self):
        return self.driver.find_element(*LoginPage.logo_label)

    def get_logo_h1_label(self):
        return self.driver.find_element(*LoginPage.logo_h1_label)

    def get_logo_para_label(self):
        return self.driver.find_element(*LoginPage.logo_para_label)

    def get_username_label(self):
        return self.driver.find_element(*LoginPage.username_label)

    def get_password_label(self):
        return self.driver.find_element(*LoginPage.password_label)

    def get_login_label(self):
        return self.driver.find_element(*LoginPage.login_label)

    def get_credential_label(self):
        return self.driver.find_element(*LoginPage.credential_label)

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_credential_box_data(self):
        return self.driver.find_element(*LoginPage.credential_data)

    def get_log_out_button(self):
        return self.driver.find_element(*LoginPage.logout_button)

