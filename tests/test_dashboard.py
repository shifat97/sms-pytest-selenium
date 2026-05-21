import pytest
import time

from pages.dashboard_page import DashboardPage
from utils.table_filter_handler import table_filter
from utils.random_payload_generator import generate_random_payload


class TestDashboard:
    def test_filter_with_department(self, driver, auth_session):
        """Test department filter with different values"""
        page = DashboardPage(driver)
        page.click(DashboardPage.STUDENTS_NAV_MENU)

        assert page.is_loaded()
        assert '/dashboard' in page.current_url

        page.page_size_dropdown("100")

        department = page.department_dropdown(page.DEPARTMENT_FILTER_BUTTON)
        page.click_filter()

        time.sleep(1)

        table_data = []

        while True:
            rows = table_filter(driver, DashboardPage.TABLE_ROW, DashboardPage.TABLE_COLUMN)
            table_data.extend(rows)

            next_btn = page.find(DashboardPage.NEXT_BUTTON)
            if next_btn.get_attribute('disabled'):
                break

            next_btn.click()

        
        for d in table_data:
            assert d["department"] == department, f'Expected {department}, Got {d["department"]} for id {d["registration_id"]}'

    
    def test_add_student_with_valid_data(self, driver, auth_session):
        """
        Add valid data → student must be created
        """
        page = DashboardPage(driver)

        page.click_add_button()
        
        # GET the random payload
        payload = generate_random_payload()
        print(payload)

        """Add the student via form"""
        page.add_student_modal(
            name = payload['name'],
            email = payload['email'],
            department = payload['department'],
            registrationId = payload['registrationId'],
            age = payload['age']
        )

        assert page.is_visible(page.STUDENT_CREATION_SUCCESS), 'Student creation message not showing'
        assert 'created' in page.get_text(page.STUDENT_CREATION_SUCCESS).lower(), 'Message is invalid'
        
    