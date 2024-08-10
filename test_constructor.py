from locators import MainPageLocators
from urls import URLS


class TestConstructorPage:
    def test_go_to_bread_success(self, driver):
        """Проверка перехода к разделу 'Булки' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.souse_button).click()
        driver.find_element(*MainPageLocators.bread_button).click()
        bread_txt = driver.find_element(*MainPageLocators.bread_txt).text
        bread_displayed = driver.find_element(*MainPageLocators.bread_ul).is_displayed()

        assert bread_txt == 'Булки' and bread_displayed

    def test_go_to_souse_success(self, driver):
        """Проверка перехода к разделу 'Соусы' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.souse_button).click()
        souse = driver.find_element(*MainPageLocators.souse_txt).text
        souse_displayed = driver.find_element(*MainPageLocators.souse_ul).is_displayed()

        assert souse == 'Соусы' and souse_displayed

    def test_go_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки' """
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.topping_button).click()
        topping = driver.find_element(*MainPageLocators.topping_txt).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert topping == 'Начинки' and topping_displayed
