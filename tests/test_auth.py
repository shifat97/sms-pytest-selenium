from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

class TestAuth:
    def test_logout(self, driver):
        """Logout Button → move to the login page"""
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.open()
        login_page.login('admin', 'password123')

        login_page.wait_for_url(dashboard_page.PATH)
        assert '/dashboard' in dashboard_page.current_url, f"Expected '/dashboard', Got {dashboard_page.current_url}"
        
        dashboard_page.logout()

        login_page.wait_for_url(login_page.PATH)
        assert '/signin' in login_page.current_url, f"Expected '/signin', Got {login_page.current_url}"
        
        assert login_page.find(login_page.TITLE).text == 'Sign In', f"Expected signin, Got something else"
         