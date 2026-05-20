from config.config import Config

class TestNavigation:
    def test_authenticated_url(self, driver):
        """High Risk: Unauthorize access"""
        urls = [
            f"{Config.BASE_URL}/dashboard/students",
            f"{Config.BASE_URL}/dashboard/teachers"
        ]

        for url in urls:
            driver.get(url)
            assert '/signin' in driver.current_url, f'Authorized url {driver.current_url} can be accessed without sign in'
            