import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with



class LoginPage:
    def __init__(self,driver):
        self.driver = driver


    # Page Locators

    makeapp_button = (By.XPATH,"//a[@id='btn-make-appointment']")
    username = (By.ID,"txt-username")
    Password = (By.NAME,"password")
    login_button = (By.XPATH,"//button[@id='btn-login']")
    error_message = (By.XPATH,"//p[@class='lead text-danger']")

    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    free_trail =(By.XPATH,"//a[normalize-space()='Start a free trial']")
    facility = (By.XPATH,"//select[@id='combo_facility']/option[3]")
    hospitaladm =(By.ID,"chk_hospotal_readmission")
    healthcare =(By.ID,"radio_program_medicare")
    visitdate =(By.ID,"txt_visit_date")
    comment = (By.ID,"txt_comment")
    bookappoint = (By.XPATH,"//button[@id='btn-book-appointment']")
    result_msg = (By.ID,"comment")


    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    # Page Actions
    def get_makeapp_button(self):
        return self.driver.find_element(*LoginPage.makeapp_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.Password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_facility(self):
        return self.driver.find_element(*LoginPage.facility)
    def get_hospitaladm(self):
        return self.driver.find_element(*LoginPage.hospitaladm)



    def get_healthcare (self):
        return self.driver.find_element(*LoginPage.healthcare)
    def get_visitdate(self):
        return self.driver.find_element(*LoginPage.visitdate)

    def set_visitdate(self, datestr):
        datefield = self.get_visitdate()
        ActionChains(self.driver).move_to_element(datefield).click().send_keys(datestr).perform()
        pass

    def get_comment(self):
        return self.driver.find_element(*LoginPage.comment)
    def get_bookappoint(self):
        return self.driver.find_element(*LoginPage.bookappoint)
    def get_result_msg(self):
        return self.driver.find_element(*LoginPage.result_msg)




    # Page Action - Main Action

    def login_to_katalon(self,usr,pwd):
        self.get_makeapp_button().click()
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_login_button().click()

    def fill_appointment_details_katalog(self, dmy, finaltxt):
        self.get_facility().click()
        self.get_hospitaladm().click()
        self.get_healthcare().click()
        self.set_visitdate(dmy)
        time.sleep(5)
        self.get_comment().click()
        self.get_comment().send_keys(finaltxt)
        self.get_bookappoint().click()



    def get_appointment_confirmation_txt_katalon(self):
        return self.get_result_msg().text

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trail(self):
        self.get_free_trail().click()