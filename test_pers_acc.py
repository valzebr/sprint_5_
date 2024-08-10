from data import MyPerson
from locators import (HeaderLocators, MainPageLocators, LoginPageLocators, RegistrationPageLocators,
                      ForgotPasswordPlaceLocators, AccountProfile)
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_in_login_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.enter_to_acc).click()
        driver.find_element(*LoginPageLocators.email_place).send_keys(MyPerson.my_email)
        driver.find_element(*LoginPageLocators.password_place).send_keys(MyPerson.my_password)
        driver.find_element(*LoginPageLocators.enter_button).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.checkout))
        checkout = driver.find_element(*MainPageLocators.checkout).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (checkout == 'Оформить заказ')

    def test_login_in_personal_account_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*HeaderLocators.personal_account_button).click()
        driver.find_element(*LoginPageLocators.email_place).send_keys(MyPerson.my_email)
        driver.find_element(*LoginPageLocators.password_place).send_keys(MyPerson.my_password)
        driver.find_element(*LoginPageLocators.enter_button).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.checkout))
        checkout = driver.find_element(*MainPageLocators.checkout).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (checkout == 'Оформить заказ')

    def test_login_in_registration_form_success(self, driver):
        """Вход в личный кабинет через форму регистрации"""
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.enter_link).click()
        driver.find_element(*RegistrationPageLocators.email_place).send_keys(MyPerson.my_email)
        driver.find_element(*RegistrationPageLocators.password_place).send_keys(MyPerson.my_password)
        driver.find_element(*LoginPageLocators.enter_button).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.checkout))
        checkout = driver.find_element(*MainPageLocators.checkout).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (checkout == 'Оформить заказ')

    def test_login_in_recover_form_success(self, driver):
        """Вход в личный кабинет через форму восстановления"""
        driver.get(URLS.FORGOT_PAGE_URL)
        driver.find_element(*ForgotPasswordPlaceLocators.enter_link).click()
        driver.find_element(*ForgotPasswordPlaceLocators.email_place).send_keys(MyPerson.my_email)
        driver.find_element(*ForgotPasswordPlaceLocators.password_place).send_keys(MyPerson.my_password)
        driver.find_element(*ForgotPasswordPlaceLocators.enter_button).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.checkout))
        checkout = driver.find_element(*MainPageLocators.checkout).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (checkout == 'Оформить заказ')


    def test_transition_to_personal_area_from_main_page_success(self, driver, get_login_driver):
        """Проверка перехода в личный кабинет с главной страницы по кнопке 'Личный кабинет' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.personal_account_button))
        driver.find_element(*HeaderLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfile.exit_button))
        save_button_displayed = driver.find_element(*AccountProfile.save_button).is_displayed()

        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_button_displayed

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver,
                                                                                           get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по клику на кнопку 'Конструктор' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.personal_account_button))
        driver.find_element(*HeaderLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfile.exit_button))
        driver.find_element(*HeaderLocators.constructor_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.bread_txt))
        bread_displayed = driver.find_element(*MainPageLocators.bread_txt).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bread_displayed

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по клику на 'Логотип' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.personal_account_button))
        driver.find_element(*HeaderLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfile.exit_button))
        driver.find_element(*HeaderLocators.logo).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.bread_txt))
        bread_displayed = driver.find_element(*MainPageLocators.bread_txt).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bread_displayed

    def test_logout_from_personal_area_success(self, driver, get_login_driver):
        """Проверка выхода из личного кабинета"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HeaderLocators.personal_account_button))
        driver.find_element(*HeaderLocators.personal_account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AccountProfile.exit_button))
        driver.find_element(*AccountProfile.exit_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.enter_button))
        login_button_displayed = driver.find_element(*LoginPageLocators.enter_button).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button_displayed