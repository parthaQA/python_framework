import time

from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils
from selenium.webdriver.common.by import By


class Checkout_screen:

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)


    tarjeta = (By.XPATH, "//p[text()='Tarjeta']")
    usar_nueva_tarjeta = (By.XPATH, "//span[text()='Usar nueva tarjeta']")
    numero_de_tarjeta = (By.ID, "cardnumberunique")
    mes_field = (By.XPATH, "//input[@data-qa='mes-input']")
    ano_field = (By.XPATH, "//input[@data-qa='expyear-input']")
    cvv_field = (By.XPATH, "//input[@data-qa='cvv-input']")
    sum_amount = (By.XPATH, "//span[@class='sumTxtAmount']")
    correo_electronico_field = (By.XPATH, "//input[@type='email']")
    pagar_con_tarjeta = (By.XPATH, "//button[@id='paylimit']")
    pop_up = (By.ID, "loginForm")
    is_iframe_displayed = (By.XPATH, "//iframe[@title='reCAPTCHA']")
    correo_email = (By.NAME, "email")
    contrasena_password = (By.NAME, "password")
    capcha = (By.XPATH, "//span[@role='checkbox']")
    click_accesso = (By.XPATH, "//button[text()='Acceso']")
    permit_notification = (By.XPATH, "//button[text()='No permitir']")
    recharge_success = (By.XPATH, "//div[@class='visual-message']")

    log = Base_class.get_logger() # creating object for log

    # this method enter all the details in checkout screen.
    def checkout_screen(self, cardnumber, month, date, cvv, email, amount):
        self.common.wait_for_visibility_element(self.tarjeta).click()
        time.sleep(2)  # some extra wait to hold the execution
        self.common.wait_for_visibility_element(self.usar_nueva_tarjeta).click()
        self.common.wait_for_visibility_element(self.numero_de_tarjeta).send_keys(cardnumber)
        self.common.wait_for_visibility_element(self.mes_field).send_keys(month)
        self.common.wait_for_visibility_element(self.ano_field).send_keys(date)
        self.common.wait_for_visibility_element(self.cvv_field).send_keys(cvv)
        self.common.wait_for_visibility_element(self.correo_electronico_field).send_keys(email)
        if self.common.wait_for_visibility_element(self.sum_amount).text == amount:
            button_enabled = self.common.wait_for_visibility_element(self.pagar_con_tarjeta)
            if button_enabled.is_enabled():
                self.common.wait_for_visibility_element(self.pagar_con_tarjeta).click()
        self.log.info("checkout done, moving to pop up screen")

 #this method enters the details in popup screen and click accesso
    def popup_screen(self, user_email, password):
        if self.common.wait_for_visibility_element(self.pop_up).is_displayed():
            self.log.info("Popup screen appears")
            self.common.wait_for_visibility_element(self.correo_email).send_keys(user_email)
            self.common.wait_for_visibility_element(self.contrasena_password).send_keys(password)
            self.common.switch_to_iframe(self.is_iframe_displayed)
            time.sleep(4) # some extra wait to hold the execution to switch frame
            self.common.wait_for_visibility_element(self.capcha).click()
            self.driver.switch_to.default_content() # returning to main frame
            self.common.set_full_screen()  # to make visible accesso button set the screen to full mode
            self.common.wait_for_visibility_element(self.click_accesso).click()

    def verify_recharge_successful(self):
        try:
            if self.common.wait_for_visibility_element(self.permit_notification).is_displayed():
                self.common.wait_for_visibility_element(self.permit_notification).click()
                self.log.info("dismissed permit notification")
        except:
            self.log.info("notifcaton button not displayed")
        success_text = self.common.wait_for_visibility_element(self.recharge_success).text
        self.log.info("captured the recharge success message")
        return success_text







