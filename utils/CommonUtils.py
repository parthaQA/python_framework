import configparser

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

    @classmethod
    def mouseHover(cls, *ele):
        element = cls.driver.find_element(*ele)
        cls.action.move_to_element(element).perform()


    def wait_for_visibility_element(self, *webelement):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(*webelement))
        return element

    @classmethod
    def switch_to_iframe(cls, frame, time_unit):
        web = WebDriverWait(cls.driver, time_unit).until(
            EC.frame_to_be_available_and_switch_to_it(frame))
        return web

    @classmethod
    def wait_for_presence_element(cls, *webelement, time_unit):
        element = WebDriverWait(cls.driver, time_unit).until(
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


    # def capture(self, name):
    #     self.driver.get_screenshot_as_file(name)
    #     allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)