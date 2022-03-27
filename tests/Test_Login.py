

import allure
import pytest

from base.Base_class import Base_class
from pages.Home import Home
from pages.Login import Login

allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("fetch_test_data_login")
class Test_Login(Base_class):

    allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, fetch_test_data_login):
        print(fetch_test_data_login)
        login = Login(self.driver)
        home = Home(self.driver)
        login.login(**fetch_test_data_login)

        home.verify_siteIds()




