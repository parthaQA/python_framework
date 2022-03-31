import configparser
import parser
import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils


#commnadline input to choose browser at runtime
#default browser is chrome if no parameter is passed
def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )



log = Base_class.get_logger()

# setup and tear down method
@pytest.fixture(scope="class")
def setup(request):
    global driver
    config = CommonUtils.read_prop_file()
    browser_name = request.config.getoption("browserName")
    if browser_name == config.get('details', 'chromeBrowser'):
        log.info("initializing chrome browser")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == config.get('details', 'firefoxBrowser'):
        log.info("initializing firefox browser")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if browser_name == None:
        log.info("please pass the browser")
        driver.quit()
    driver.maximize_window()
    log.info("Launch undostres application and open home page")
    driver.get(config.get('details', 'url'))
    request.cls.driver = driver
    yield driver  # Run all other pytest_runtest_makereport non wrapped hooks
    driver.quit()


#this hooks takes the screenshot when test case is failed
#and attached it to allure report
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




