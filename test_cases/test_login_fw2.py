import pytest
from pageObjects.login_page import Login
from utilities.read_properties import ReadConfig
from utilities.custom_loggers import LogGen

class TestLogin:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_login_001(self, setup):
        self.logger.info("****** Test Login Started *********")
        self.logger.info("****** Test Verifying Title Page *********")
        self.page = setup
        self.page.goto(self.base_url)
        self.lp = Login(self.page)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()

        try:
            expected_title = "Swag Labs"
            actual_title = self.page.title()
            assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
            self.logger.info("****** Title Verified *********")
        except AssertionError as e:
            self.page.screenshot(path="screenshots/title.png")
            raise e
        finally:
            self.page.close()
        self.logger.info("****** Test Login Completed *********")
