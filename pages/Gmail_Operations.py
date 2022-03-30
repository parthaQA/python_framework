import time

from selenium.webdriver.common.by import By
from datetime import datetime
from base.Base_class import Base_class
from utils.CommonUtils import CommonUtils


class Gmail_Operations:


    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)
        self.logger = Base_class.get_logger()
        self.get_time = self.common.current_time()



    user_email = (By.ID, "identifierId")
    u_next = (By.XPATH, "//span[text()='Next']")
    user_password = (By.XPATH, "//input[@name='password']")
    pass_next = (By.XPATH, "//span[text()='Next']")
    verify_login_success = (By.XPATH, "//*[text()='Compose']")
    subject = (By.NAME,'subjectbox')
    body = (By.CSS_SELECTOR, "div[aria-label='Message Body']")
    button = (By.XPATH, "//div[@aria-label='More options']/child::div[2]")
    label = (By.XPATH, "//*[text()='Label']")
    social = (By.XPATH, "//div[@title='Social']")
    to = (By.XPATH, "//textarea[@name='to']")
    send = (By.XPATH, "//*[text()='Send']")
    received_email = (By.XPATH, "//span[@class ='bq3']")
    social_tab = (By.XPATH, "//*[text()='Social']")
    mark_starred = (By.XPATH, "//tr[@role='row']/child::td[3]/child::span")
    get_email_subject = (By.XPATH, "//div[text()='Inbox']/preceding::h2[1]")
    get_email_body = (By.XPATH, "//div[@style='display:']/child::div[2]/child::div[3]")
    is_socialtab_selected = (By.XPATH, "//div[@aria-label='Social']")

    # This method will login to gmail
    def gmail_login(self):
        self.common.wait_for_visibility_element(self.user_email).send_keys("test.sen92@gmail.com")
        self.common.wait_for_visibility_element(self.u_next).click()
        self.common.wait_for_visibility_element(self.user_password).send_keys("Asdf#1234")
        self.common.wait_for_visibility_element(self.pass_next).click()

    # This method will verify login success or not
    def login_success(self):
        time.sleep(10)
        try :
            if self.common.wait_for_presence_element(self.verify_login_success).is_displayed():
                return True
        except:
            Exception("test failed")

    # This method will compose the email
    def compose_email(self):
        self.common.wait_for_visibility_element(self.verify_login_success).click()
        time.sleep(3) #some wait time to hold the execution
        self.common.wait_for_visibility_element(self.to).send_keys("test.sen92@gmail.com")
        self.common.wait_for_visibility_element(self.button).click()
        self.common.wait_for_visibility_element(self.label).click()
        time.sleep(3) #some wait time to hold the execution
        self.common.wait_for_visibility_element(self.social).click()
        self.common.wait_for_visibility_element(self.subject).send_keys("Test Mail")
        self.common.wait_for_visibility_element(self.body).send_keys("Test Email Body")

    # This method sends the email
    def send_email(self):
        self.common.wait_for_visibility_element(self.send).click()

    # This method click social tab and verify socail tab is opened or not
    def open_social_tab(self):
        self.common.wait_for_visibility_element(self.social_tab).click()
        is_selected = self.common.wait_for_visibility_element(self.is_socialtab_selected).get_attribute('aria-selected')
        if is_selected == "true":
            return True

    # This method mark the received email as starred and it takes email subject as argument
    def mark_starred_mail(self, text):
        time.sleep(4)
        webelement_received_mail = self.driver.find_element(By.XPATH, "//*[text()='"+text+"']/ancestor::tr")
        webelement_starred = self.driver.find_element(By.XPATH, "//*[text()='"+text+"']/ancestor::tr/td[3]")
        if webelement_received_mail.is_displayed():
            try:
                webelement_starred.click()
            except:
                Exception("element not found")

    # This method opens the email and it takes email body as  argument
    def open_email(self, text):
        get_time = self.common.current_time()
        webelement_body = self.driver.find_element(By.XPATH, "//*[text()='"+text+"']/ancestor::tr")
        if webelement_body.is_displayed() and self.get_time<get_time:
            try:
                webelement_body.click()
                if self.common.wait_for_visibility_element(self.get_email_subject).is_diplayed():
                    self.logger.info("email opened")

            except:
                Exception("mail not opened")

    # This method verifies email subject
    def verify_email_subject(self):
        get_subject = self.common.wait_for_visibility_element(self.get_email_subject).text
        return get_subject

    # This method verifies email body
    def verify_email_body(self):
        get_body = self.common.wait_for_visibility_element(self.get_email_body).text
        return get_body








