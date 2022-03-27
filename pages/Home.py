import time

from selenium.webdriver.common.by import By

from utils.CommonUtils import CommonUtils


class Home:


    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)

    select_dropdown = (By.XPATH, "//*[text()='Select an Org']")
    site_ids = (By.XPATH, "//*[@class='mat-option-text']")




    def verify_homePage(self):
        pass


    def verify_siteIds(self):
        time.sleep(15)
        self.common.wait_for_visibility_element(self.select_dropdown).click()
        print("-----------------------------------------------------------------------------")
        get_ids = self.driver.find_elements(*self.site_ids)
        id_list = []
        dic = {}
        len_site = len(get_ids) + 1
        for i in get_ids:
            len_site -=1
            dic[len_site]= i.text
        print(dic)
        # li = self.driver.find_elements(By.CSS_SELECTOR, "mat-option[id^='mat-option']")
        # print(len(li))
        # for j in range(len(li)):
        #     id_list.append(self.driver.find_element(By.ID, "mat-option-"+str(j)).text)
        # print(id_list)
        d = {}
        for key, value in dic.items():
            d.setdefault(value,set()).add(key)
        l = [key for key, values in d.items() if len(values) > 1]
        print(l)
