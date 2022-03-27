import configparser
import time

import pytest
import allure
from allure_commons.types import AttachmentType
from bson import ObjectId
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils
from utils.DB_Utils import DB_Utils

#driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )

log = Base_class.get_logger()

@pytest.fixture()
def fetch_test_data_login():
    data = DB_Utils.db_connect()
    record = data.find_one({"_id": ObjectId("507f191e810c19729de860ea")}, {'_id': 0})
    log.info("values ::: ", record)
    return record

@pytest.fixture()
def fetch_test_data_generate_token():
    data = DB_Utils.db_connect()
    i = {}
    record = data.find_one({"_id": ObjectId("621f8af972e8744c1c25f2d1")}, {'_id': 0})
    log.info("values ::: ", record)
    return record


@pytest.fixture(scope="class")
def setup(request):
    global driver
   # config = configparser.RawConfigParser()
    # config.read("../properties/environment.properties")
    config = CommonUtils.read_prop_file()
    browser_name = request.config.getoption("browserName")
    if browser_name == config.get('details', 'chromeBrowser'):
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == config.get('details', 'firefoxBrowser'):
        driver = webdriver.Firefox(GeckoDriverManager().install())

    driver.maximize_window()
    driver.get(config.get('details', 'url'))
    request.cls.driver = driver
    yield driver  # Run all other pytest_runtest_makereport non wrapped hooks
    time.sleep(2)
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    file_name = ""
    #logger = Base_class.get_logger()
    report = outcome.get_result()
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                file_name = report.nodeid.replace("::", "_") + ".png"
                log.info(file_name)
                if file_name is not None:
                    allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)

            except Exception as e:
                print(f"unable to take screenshot as {file_name} is not found")




