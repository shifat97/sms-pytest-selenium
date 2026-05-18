import pytest
import time

from config.config import Config
from pages.dashboard_page import DashboardPage

class TestDashboard:
    def test_filter_with_department(self, driver, auth_session):
        """Test department filter with different values"""
        page = DashboardPage(driver)
        page.click(DashboardPage.STUDENTS_NAV_MENU)

        assert page.is_loaded()
        assert '/dashboard' in page.current_url

        page.page_size_dropdown("100")
        time.sleep(1)
        department = page.department_dropdown()
        page.click(DashboardPage.FILTER_BUTTON)
        time.sleep(1)

        table_data = []
        while True:
            rows = page.table_filter()
            table_data.extend(rows)          

            next_btn = page.find(DashboardPage.NEXT_BUTTON)
            if next_btn.get_attribute('disabled'):
                break                        

            next_btn.click()
            time.sleep(1) 
        
        for d in table_data:
            assert d["department"] == department, f'Expected {department}, Got {d["department"]} for id {d["registration_id"]}'

    