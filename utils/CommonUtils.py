import configparser
import time

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

    # This method wait for element present in DOM and also visible
    def wait_for_visibility_element(self, *webelement):
        return self.wait.until(
            EC.visibility_of_element_located(*webelement))

    # this method search for iframe and then switches to it
    def switch_to_iframe(self, frame):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(frame))

    # set the screen to full to avoid any screen size issue.
    def set_full_screen(self):
        self.driver.fullscreen_window()

    # this mehtod search for element present in DOM
    def wait_for_presence_element(self, *webelement):
        return self.wait.until(
            EC.presence_of_element_located(*webelement))

    # this method return true if title is found else returns false
    def title_is(self, title):
        return self.wait.until(
            EC.title_contains(title))

    # this method reads the property file
    @classmethod
    def read_prop_file(cls):
        config = configparser.RawConfigParser()
        config.read("../properties/environment.properties")
        return config
