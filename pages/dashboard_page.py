import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    PATH = '/dashboard/students'
    DASHBOARD_TITLE = (By.XPATH, "//div//h1[text()='Students']")
    LOGOUT_BTN = (By.XPATH, "//div[@data-sidebar='footer']//button")
    STUDENTS_NAV_MENU = (By.XPATH, "//ul//li//a[.//span[text()='Students']]")
    SELECT_PAGE_SIZE = (By.XPATH, "//div//select")
    DEPARTMENT_FILTER_BUTTON = (By.XPATH, "//button[@role='combobox']")
    FILTER_OPTIONS = (By.XPATH, "//div[@role='option']")
    FILTER_BUTTON = (By.XPATH), "//button[text()='Filter']"
    TABLE_ROW = (By.XPATH, "//table//tbody//tr")
    TABLE_COLUMN = (By.XPATH, "./td")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")

    def is_loaded(self):
        return self.is_visible(self.DASHBOARD_TITLE)

    def get_page_title(self):
        return self.get_text(self.DASHBOARD_TITLE)

    def logout(self):
        self.click(self.LOGOUT_BTN)
        return self

    def page_size_dropdown(self, page_size):
        self.select_by_value(self.SELECT_PAGE_SIZE, page_size)
        return self
    
    def department_dropdown(self):
        self.click(self.DEPARTMENT_FILTER_BUTTON)
        departments = self.find_elements(self.FILTER_OPTIONS)
        department = random.choice(departments)
        selected_value = department.text
        department.click()
        return selected_value

    def table_filter(self):
        rows = self.find_elements(DashboardPage.TABLE_ROW)
        table_dict = []

        for row in rows:
            column = row.find_elements(*self.TABLE_COLUMN) 
            row_data = {
                "name": column[0].text,
                "email": column[1].text,
                "department": column[2].text,
                "registration_id": column[3].text,
                "age": column[4].text
            }
            table_dict.append(row_data)

        return table_dict
    