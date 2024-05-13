import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from katalontests.pageObjects.katalonloginpage import LoginPage
from katalontests.pageObjects.makeappPage import MakeappPage
from allure_commons.types import AttachmentType


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    return driver


@allure.epic("Katalon Login Test")
@allure.feature("TC#0 - katalon App Negative Test")
@pytest.mark.negative
def test_katalon_login_negative(setup):
    driver = setup
    katalonloginpage = LoginPage(driver)
    katalonloginpage.login_to_katalon(usr="py2x@thetestingacademy.com",pwd="Wingify@1234")
    time.sleep(5)
    error_message = katalonloginpage.get_error_message_text()
    allure.attach(driver.get_screenshot_as_png(),name="login page with error msg screenshot")
    assert error_message == "Login failed! Please ensure the username and password are valid."


@allure.epic("katalon Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_katalon_login_positive(setup):
    driver = setup
    katalonloginpage = LoginPage(driver)
    allure.attach(driver.get_screenshot_as_png(), name="login-Screenshot", attachment_type=AttachmentType.PNG)
    katalonloginpage.login_to_katalon(usr="John Doe",pwd="ThisIsNotAPassword")
    time.sleep(5)
    comment = "I need an appointment for above date"
    allure.attach(driver.get_screenshot_as_png(), name=" filldetails-Screenshot", attachment_type=AttachmentType.PNG)
    katalonloginpage.fill_appointment_details_katalog(dmy='10/05/2024', finaltxt=comment)
    txt = katalonloginpage.get_appointment_confirmation_txt_katalon()

    assert txt == comment
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name=" bookappointment-Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)


    makeappPage = MakeappPage(driver)
    makeappPage.logoff_katalon()


