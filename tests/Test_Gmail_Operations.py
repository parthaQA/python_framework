import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.Base_class import Base_class
from pages.Gmail_Operations import Gmail_Operations
from utils.CommonUtils import CommonUtils
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.gmail
class Test_Gmail_Operations(Base_class):

    expected_subject = "Test Mail"
    expected_email_body = "Test Email Body"
    def test_Gmail_Operations(self):
        log = self.get_logger()
        login = Gmail_Operations(self.driver)
        login.gmail_login()
        verify_success = login.login_success()
        log.info("Login Successful")
        assert verify_success
        login.compose_email()
        login.send_email()
        log.info("email sent")
        is_emailIn_social = login.open_social_tab()
        assert is_emailIn_social
        log.info("verified email is in social tab")
        login.mark_starred_mail(self.expected_subject)
        login.open_email(self.expected_email_body)
        email_subject = login.verify_email_subject()
        assert email_subject == self.expected_subject
        log.info("verified email subject")
        email_body = login.verify_email_body()
        assert email_body == self.expected_email_body
        log.info("verfied email body")


