import time

from selenium.webdriver.common.by import By

from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils


class Home_Screen:


    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)

    operador = (By.XPATH, "//input[@name='operator']")
    drop_down = (By.XPATH, "//div[@class='suggestion']")
    numero_de_celular = (By.XPATH, "//input[@name='mobile']")
    monto_de_Recarga = (By.XPATH, "//input[@name='amount']")
    click_siguiente = (By.XPATH, "//button[@perform='payment']")

    log = Base_class.get_logger() # creating object for log


    #this method verfies home screen
    def verify_home_screen(self, page_title):
        actual_title = self.common.title_is(page_title)
        self.log.info("title is verified")
        return actual_title


    #this method choose operator and enter recharge amount
    def home_screen(self, telcel, phone_number, amount):
        self.common.wait_for_visibility_element(self.operador).click()
        select_telcel = (By.XPATH, "//b[text()='"+telcel+"']")
        self.common.wait_for_visibility_element(select_telcel).click()
        self.common.wait_for_visibility_element(self.numero_de_celular).send_keys(phone_number)
        self.common.wait_for_visibility_element(self.monto_de_Recarga).click()
        select_recarga = (By.XPATH, "//b[text()='"+"$"+""+amount+"']")
        self.common.wait_for_visibility_element(select_recarga).click()
        self.common.wait_for_visibility_element(self.click_siguiente).click()
        self.log.info("navigating to checkout screen")














