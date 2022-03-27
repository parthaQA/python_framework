import pytest

from base.Base_class import Base_class
from pages.Login import Login

@pytest.mark.skip
@pytest.mark.usefixtures("fetch_test_data")
class Test_sample(Base_class):

    def test_edit(self, fetch_test_data):
        print(fetch_test_data)
        login = Login(self.driver)
        login.login(**fetch_test_data)