from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utility.test_setup import TestSetup


class SideBar:
    sidebar_items    = (By.CSS_SELECTOR, ".sidebar-item")
    sidebar = (By.ID, "sidebar")
    sidebar_title = (By.XPATH, "//div[@class='sidebar-title']")
    profile = (By.XPATH, "//a[text()=' Profile']")
    about = (By.XPATH, "//a[text()=' About Me']")
    availability = (By.XPATH, "//a[text()=' Availability']")
    skills = (By.XPATH, "//a[text()=' Skills Explorer']")
    domain_experience = (By.XPATH, "//a[text()=' Domain Experience']")
    type = (By.XPATH, "//a[text()=' Testing Types']")
    work_experience =(By.XPATH, "//a[text()=' Work Experience']")
    education = (By.XPATH, "//a[text()=' Education']")
    certification = (By.XPATH, "//a[text()=' Certifications']")
    tools = (By.XPATH, "//a[text()=' Tools & Tech']")
    quick_action = (By.XPATH, "//a[text()= ' Quick Actions']")
    contact = (By.XPATH, "//a[text()=' Contact']")
    hero_section = (By.ID, "sec-hero")
    about_section = (By.ID, "sec-about")
    availability_section = (By.ID, "sec-availability")
    skills_section = (By.ID, "sec-skills")
    d_experience_section = (By.ID, "sec-domain")
    testing_type_section = (By.ID, "sec-testing")
    experience_section = (By.ID, "sec-experience")
    education_section = (By.ID, "sec-education")
    certification_section = (By.ID, "sec-certifications")
    tools_tech_section = (By.ID, "sec-tools")
    action_section = (By.ID, "sec-actions")
    message_section = (By.ID, "sec-contact")

    def __init__(self, driver):
        self.driver = driver

    def verify_side_bar_visibility(self):
        return self.driver.find_element(*SideBar.sidebar)

    def verify_sidebar_number_of_items(self):
        return self.driver.find_elements(*SideBar.sidebar_items)

    def verify_sidebar_title(self):
        return self.driver.find_element(*SideBar.sidebar_title)

    def verify_profile(self):
        return self.driver.find_element(*SideBar.profile)

    def verify_is_hero_section_visible(self):
        hero_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.hero_section)
        )
        return self.driver.find_elements(By.CSS_SELECTOR, "#sidebar a")

    def verify_about(self):
        return self.driver.find_element(*SideBar.about)

    def verify_is_about_section_visible(self):
        about_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.about_section)
        )
        return about_element.is_displayed()

    def verify_availability(self):
        return self.driver.find_element(*SideBar.availability)

    def verify_current_availability_section_visible(self):
        availability_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.availability_section)
        )
        return availability_element.is_displayed()

    def verify_skills(self):
        return self.driver.find_element(*SideBar.skills)

    def verify_technical_skills_section_visible(self):
        skills_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.skills_section)
        )
        return skills_element.is_displayed()

    def verify_domain_experience(self):
        return self.driver.find_element(*SideBar.domain_experience)

    def verify_domain_experience_section_visible(self):
        experience_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.d_experience_section)
        )
        return experience_element.is_displayed()

    def verify_type(self):
        return self.driver.find_element(*SideBar.type)

    def verify_testing_expertise_section_visible(self):
        testing_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.testing_type_section)
        )
        return testing_element.is_displayed()

    def verify_work_experience(self):
        return self.driver.find_element(*SideBar.work_experience)

    def verify_work_experience_section_visible(self):
        experience_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.experience_section)
        )
        return experience_element.is_displayed()

    def verify_education(self):
        return self.driver.find_element(*SideBar.education)

    def verify_education_section_visible(self):
        education_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.education_section)
        )
        return education_element.is_displayed()

    def verify_certification(self):
        return self.driver.find_element(*SideBar.certification)

    def verify_certification_section_visible(self):
        certification_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.certification_section)
        )
        return certification_element.is_displayed()

    def verify_tools(self):
        return self.driver.find_element(*SideBar.tools)

    def verify_tools_and_tech_section_visible(self):
        tools_tech_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.tools_tech_section)
        )
        return tools_tech_element.is_displayed()

    def verify_quick_action(self):
        return self.driver.find_element(*SideBar.quick_action)

    def verify_quick_action_section_visible(self):
        action_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.action_section)
        )
        return action_element.is_displayed()

    def verify_contact(self):
        return self.driver.find_element(*SideBar.contact)

    def verify_send_a_message_section_visible(self):
        message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.message_section)
        )
        return message_element.is_displayed()

    def get_sidebar_position(self):
        sidebar_element = self.driver.find_element(*self.sidebar)
        return self.driver.execute_script("""
                const rect = arguments[0].getBoundingClientRect();
                return {top: rect.top, left: rect.left};
            """, sidebar_element)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")


























