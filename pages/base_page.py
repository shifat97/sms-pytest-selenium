from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def visit(self, path=''):
        self.driver.get(Config.BASE_URL + path)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def type_text(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        return self

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_url(self, fragment):
        self.wait.until(EC.url_contains(fragment))
        return self

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def title(self):
        return self.driver.title
