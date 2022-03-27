import pytest
from selenium.webdriver.common.by import By

from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)

    user_id_field = (By.ID, "username")
    submit_button = (By.ID, "user-submit")
    user_id_field_1 = (By.ID, "username")
    password_field = (By.ID, "password")
    continue_button = (By.XPATH, "//button[@type='submit']")

    def login(self, **fetch_test_data):
        logger = Base_class.get_logger()
        self.common.wait_for_visibility_element(self.user_id_field).send_keys(fetch_test_data["ui_email"])
        self.common.wait_for_visibility_element(self.submit_button).click()
        self.common.wait_for_visibility_element(self.user_id_field_1).send_keys(fetch_test_data["ui_email"])
        self.common.wait_for_visibility_element(self.continue_button).click()
        self.common.wait_for_visibility_element(self.password_field).send_keys(fetch_test_data["ui_password"])
        self.common.wait_for_visibility_element(self.continue_button).click()
        logger.info("Login successful")


