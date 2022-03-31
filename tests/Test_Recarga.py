import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.Base_class import Base_class
from pages.Checkout_screen import Checkout_screen
from pages.Home_Screen import Home_Screen


@pytest.mark.recarga
class Test_Recarga(Base_class):

    page_title = "UnDosTres"
    phone_number = "8465433546"
    mobile_operator = "Telcel"
    card_number = "4111111111111111"
    month = "11"
    date = "25"
    cvv =  "111"
    email = "test@test.com"
    amount = "10"
    user_email = "automationexcersise@test.com"
    password = "123456"

    def test_recarga(self):
        home = Home_Screen(self.driver)
        checkout = Checkout_screen(self.driver)
        log = self.get_logger()
        title = home.verify_home_screen(self.page_title)
        assert title
        home.home_screen(self.mobile_operator,self.phone_number, self.amount)
        checkout.checkout_screen(self.card_number,self.month, self.date, self.cvv, self.email, self.amount)
        checkout.popup_screen(self.user_email, self.password)
        actual_text = checkout.verify_recharge_successful()  #verify recharge is successful or not
        assert actual_text == "¡Recarga Exitosa!"
        log.info("test case execution is completed")