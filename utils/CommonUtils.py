import configparser
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setup")
class CommonUtils:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 30)

    @classmethod
    def mouseHover(cls, *ele):
        element = cls.driver.find_element(*ele)
        cls.action.move_to_element(element).perform()

    # This method wait for the visiblity of element
    def wait_for_visibility_element(self, *webelement):
        element = self.wait.until(
            EC.visibility_of_element_located(*webelement))
        return element

    @classmethod
    def switch_to_iframe(cls, frame, time_unit):
        web = WebDriverWait(cls.driver, time_unit).until(
            EC.frame_to_be_available_and_switch_to_it(frame))
        return web


    def wait_for_presence_element(self, *webelement):
        element = self.wait.until(
            EC.presence_of_element_located(*webelement))
        return element

    @classmethod
    def element_to_be_clickable(cls, *webelement, time_unit):
        element = WebDriverWait(cls.driver, time_unit).until(
            EC.element_to_be_clickable(*webelement))
        return element

    @classmethod
    def alert_is_present(cls, time_unit):
        element = WebDriverWait(cls.driver, time_unit).until(
            EC.alert_is_present())
        return element

    @classmethod
    def title_is(cls, title, time_unit):
        element = WebDriverWait(cls.driver, time_unit).until(
            EC.title_is(title))
        return element

    @classmethod
    def read_prop_file(cls):
        config = configparser.RawConfigParser()
        config.read("../properties/environment.properties")
        return config

    def move_element_to(self, *webelement):
        return self.action.move_to_element(*webelement)

    # This method calculates current time and returns it
    def current_time(self):
        now = datetime.now()
        print("now =", now)
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string.split(" ")[1]
