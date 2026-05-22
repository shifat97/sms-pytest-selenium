import time

import pytest

from pages.dashboard_page import DashboardPage
from utils.random_payload_generator import generate_random_payload
from utils.table_filter_handler import table_filter


class TestDashboard:
    @pytest.mark.smoke
    def test_add_student_with_valid_data(self, driver, auth_session):
        """
        Add valid data → student must be created
        """
        page = DashboardPage(driver)

        page.click_add_button()

        # GET the random payload
        payload = generate_random_payload()

        """Add the student via form"""
        page.add_student_modal(
            name=payload['name'],
            email=payload['email'],
            department=payload['department'],
            registrationId=payload['registrationId'],
            age=payload['age']
        )

        assert page.is_visible(page.STUDENT_CREATION_SUCCESS), 'Student creation message not showing'
        assert 'created' in page.get_text(page.STUDENT_CREATION_SUCCESS).lower(), 'Message is invalid'

    @pytest.mark.smoke
    def test_search_with_name_student_after_creation(self, driver, auth_session):
        """Add user → pick the name → filter → name is shown in the table"""
        page = DashboardPage(driver)

        page.click_add_button()
        payload = generate_random_payload()

        """Add the student via form"""
        page.add_student_modal(
            name=payload['name'],
            email=payload['email'],
            department=payload['department'],
            registrationId=payload['registrationId'],
            age=payload['age']
        )

        assert page.is_visible(page.STUDENT_CREATION_SUCCESS), 'Student creation message not showing'

        # Wait for modal to be close
        page.wait_until_invisible(DashboardPage.MODAL)

        page.search_student_with_name(payload['name'])
        time.sleep(1)

        results = table_filter(driver, DashboardPage.TABLE_ROW, DashboardPage.TABLE_COLUMN)
        for data in results:
            assert payload['name'] in data['name'], f"Expected {payload['name']}, Got {data['name']}"

    @pytest.mark.smoke
    def test_search_with_email_student_after_creation(self, driver, auth_session):
        """Add user → pick the email → filter → email is shown in the table"""
        page = DashboardPage(driver)

        page.click_add_button()
        payload = generate_random_payload()

        """Add the student via form"""
        page.add_student_modal(
            name=payload['name'],
            email=payload['email'],
            department=payload['department'],
            registrationId=payload['registrationId'],
            age=payload['age']
        )

        assert page.is_visible(page.STUDENT_CREATION_SUCCESS), 'Student creation message not showing'

        # Wait for modal to be close
        page.wait_until_invisible(DashboardPage.MODAL)

        page.search_student_with_email(payload['email'])
        time.sleep(1)

        result = table_filter(driver, DashboardPage.TABLE_ROW, DashboardPage.TABLE_COLUMN)
        assert len(result) == 1, f"Expected 1 result, Got {len(result)}"
        assert payload['email'] in result[0]['email'], f"Expected {payload['email']}, Got {result[0]['email']}"
        assert payload['email'] == result[0]['email'], f"Expected {payload['email']}, Got {result[0]['email']}"

    @pytest.mark.smoke
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
            assert d[
                       "department"] == department, f'Expected {department}, Got {d["department"]} for id {d["registration_id"]}'

    @pytest.mark.smoke
    def test_search_with_registration_id_after_creation(self, driver, auth_session):
        """Add user → pick the registration id → filter → user with created id shown in the table"""
        page = DashboardPage(driver)

        page.click_add_button()
        payload = generate_random_payload()

        """Add the student via form"""
        page.add_student_modal(
            name=payload['name'],
            email=payload['email'],
            department=payload['department'],
            registrationId=payload['registrationId'],
            age=payload['age']
        )

        assert page.is_visible(page.STUDENT_CREATION_SUCCESS), 'Student creation message not showing'

        # Wait for modal to be close
        page.wait_until_invisible(DashboardPage.MODAL)

        page.search_student_with_registration_id(payload['registrationId'])
        time.sleep(1)

        result = table_filter(driver, DashboardPage.TABLE_ROW, DashboardPage.TABLE_COLUMN)
        assert len(result) == 1, f"Expected 1 result, Got {len(result)}"
        assert int(payload['registrationId']) == int(result[0]['registrationId']), \
                f"Expected {int(payload['registrationId'])}, Got {int(result[0]['registrationId'])}"
