from selenium.webdriver.common.by import By

import time
class MakeappPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    toggle = (By.ID, "menu-toggle")
    logout = (By.LINK_TEXT, "Logout")

    def get_toggle(self):
        return self.driver.find_element(*MakeappPage.toggle)

    def get_logout(self):
        return self.driver.find_element(*MakeappPage.logout)

    def logoff_katalon(self):
        self.get_toggle().click()
        time.sleep(5)
        self.get_logout().click()
        time.sleep(5)





