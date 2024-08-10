from data import MyPerson, MyRandomData
from locators import RegistrationPageLocators, LoginPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPage:

    def test_registration_success(self, driver):
        """Проверка регистрации пользователя"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_button))
        driver.find_element(*RegistrationPageLocators.name_place).send_keys(MyRandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_place).send_keys(MyRandomData.rand_email)
        driver.find_element(*RegistrationPageLocators.password_place).send_keys(MyRandomData.rand_password)
        driver.find_element(*RegistrationPageLocators.registration_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.enter_button))
        login_button_displayed = driver.find_element(*LoginPageLocators.enter_button).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        """Проверка регистрации пользователя с некорректным паролем (менее 6 символов)"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_button))
        driver.find_element(*RegistrationPageLocators.name_place).send_keys(MyPerson.my_name)
        driver.find_element(*RegistrationPageLocators.email_place).send_keys(MyPerson.my_email)
        driver.find_element(*RegistrationPageLocators.password_place).send_keys(12345)
        driver.find_element(*RegistrationPageLocators.registration_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_any_elements_located(RegistrationPageLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)