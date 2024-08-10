from selenium import webdriver
import pytest
from locators import LoginPageLocators
from urls import URLS
from data import MyPerson


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.AUTH_PAGE_URL)
    driver.find_element(*LoginPageLocators.email_place).send_keys(MyPerson.my_email)
    driver.find_element(*LoginPageLocators.password_place).send_keys(MyPerson.my_password)
    driver.find_element(*LoginPageLocators.enter_button).click()

    return driver
