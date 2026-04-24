import pytest

from PageObject.side_bar import SideBar
from utility.test_setup import TestSetup


@pytest.mark.sidebar
class TestSideBar(TestSetup):
#TC_SIDEBAR_001 — Verify sidebar is visible after login on the portfolio page
    def test_sidebar_visibility(self):
        sidebar_visibility = SideBar(self.driver)
        assert sidebar_visibility.verify_side_bar_visibility().is_displayed(), "Sidebar is not visible"

#TC_SIDEBAR_002 - Verify title of Sidebar
    def test_sidebar_title(self):
        title = SideBar(self.driver)
        assert title.verify_sidebar_title().is_displayed(), "Sidebar title is wrong"

#TC_SIDEBAR_003 — Verify sidebar item Profile scrolls to the Hero section
    def test_profile_to_hero_section(self):
        hero = SideBar(self.driver)
        hero.verify_profile().click()
        assert hero.verify_is_hero_section_visible(), "Hero Section is not visible on clicking Profile in Sidebar"

#TC_SIDEBAR_004 — Verify sidebar item About Me scrolls to the About Me section
    def test_about_me_to_about_section(self):
        about_me = SideBar(self.driver)
        about_me.verify_about().click()
        assert about_me.verify_is_about_section_visible(), "About Me section is not visible on clicking About Me in Sidebar"

#TC_SIDEBAR_005 — Verify sidebar item Availability scrolls to Current Availability section
    def test_availability_to_current_availability_section(self):
        c_availability = SideBar(self.driver)
        c_availability.verify_availability().click()
        assert c_availability.verify_current_availability_section_visible(), "Current Availability section is not visible on clicking Availability in Sidebar"

#TC_SIDEBAR_006 — Verify sidebar item Skills Explorer scrolls to Technical Skills section
    def test_skills_explorer_to_technical_skills_section(self):
        technical_skills = SideBar(self.driver)
        technical_skills.verify_skills().click()
        assert technical_skills.verify_technical_skills_section_visible(), "Technical Skills section is not visible on clicking Skills Explorer in Sidebar"

#TC_SIDEBAR_007 — Verify sidebar item Domain Experience scrolls to Domain Experience section
    def test_domain_experience_to_domain_experience_section(self):
        domain_experience = SideBar(self.driver)
        domain_experience.verify_domain_experience().click()
        assert domain_experience.verify_domain_experience_section_visible(), "Domain Experience section is not visible on clicking Domain Experience in Sidebar"

#TC_SIDEBAR_008 — Verify sidebar item Testing Types scrolls to Testing Expertise section
    def test_testing_types_to_testing_expertise_section(self):
        testing_expertise = SideBar(self.driver)
        testing_expertise.verify_type().click()
        assert testing_expertise.verify_testing_expertise_section_visible(), "Testing Expertise section is not visible on clicking Testing Types in Sidebar"

#TC_SIDEBAR_009 — Verify sidebar item Work Experience scrolls to Work Experience section
    def test_work_experience_to_work_experience_section(self):
        work_experience = SideBar(self.driver)
        work_experience.verify_work_experience().click()
        assert work_experience.verify_work_experience_section_visible(), "Work Experience section is not visible on clicking Work Experience in Sidebar"

#TC_SIDEBAR_010 — Verify sidebar item Education scrolls to Education section
    def test_education_to_education_section(self):
        education = SideBar(self.driver)
        education.verify_education().click()
        assert education.verify_education_section_visible(), "Education section is not visible on clicking Education in Sidebar"

#TC_SIDEBAR_011 — Verify sidebar item Certifications scrolls to Certifications section
    def test_certification_to_certification_and_courses_section(self):
        certification = SideBar(self.driver)
        certification.verify_certification().click()
        assert certification.verify_certification_section_visible(), "Certification and Courses section is not visible on clicking Certification in Sidebar"

#TC_SIDEBAR_012 — Verify sidebar item Tools & Tech scrolls to Tools & Technologies section
    def test_tools_tech_to_tools_technology_section(self):
        tools = SideBar(self.driver)
        tools.verify_tools().click()
        assert tools.verify_tools_and_tech_section_visible(), "Tools and Technology section is not visible on clicking Tools in Sidebar"

#TC_SIDEBAR_013 — Verify sidebar item Quick Actions scrolls to Quick Actions section
    def test_quick_action_to_quick_action_section(self):
        quick_action = SideBar(self.driver)
        quick_action.verify_quick_action().click()
        assert quick_action.verify_quick_action_section_visible(), "Quick Action section is not visible on clicking Quick Action in Sidebar"

#TC_SIDEBAR_014 — Verify sidebar item Contact scrolls to Send a Message section
    def test_contact_send_a_message_section(self):
        message = SideBar(self.driver)
        message.verify_contact().click()
        assert message.verify_send_a_message_section_visible(), "Send a Message section is not visible on clicking Contact in Sidebar"

#TC_SIDEBAR_015 — Verify sidebar remains sticky/fixed while scrolling down the page
    def test_sidebar_is_sticky(self):
        page = SideBar(self.driver)
        initial_position = page.get_sidebar_position()
        page.scroll_down()
        after_scroll_position = page.get_sidebar_position()
        assert initial_position == after_scroll_position, "Sidebar is not sticky/fixed while scrolling"







