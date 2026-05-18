from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    PATH = '/dashboard'
    DASHBOARD_TITLE = (By.XPATH, "//div//h1[text()='Students']")
    LOGOUT_BTN = (By.ID, "//div[@data-sidebar='footer']//button")
    NAV_MENU = (By.XPATH, "//div//ul[@data-sidebar='menu']")

    def is_loaded(self):
        return self.is_visible(self.DASHBOARD_TITLE)

    def get_page_title(self):
        return self.get_text(self.DASHBOARD_TITLE)

    def logout(self):
        self.click(self.LOGOUT_BTN)
        return self
