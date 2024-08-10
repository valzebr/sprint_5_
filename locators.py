from selenium.webdriver.common.by import By


class HeaderLocators:
    """Шапка сайта"""
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка "Конструктор"
    order_feed = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # кнопка "Лента Заказов"
    logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип stellar burger
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"


class MainPageLocators:
    """Главная страница"""
    bread_button = (By.XPATH, ".//span[text() = 'Булки']")  # кнопка  "Булки"
    souse_button = (By.XPATH, ".//span[text() = 'Соусы']")  # кнопка "Соусы"
    topping_button = (By.XPATH, ".//span[text() = 'Начинки']")  # кнопка  "Начинки"
    bread_txt = (By.XPATH, ".//h2[text() = 'Булки']")  # Текст "Булки"
    souse_txt = (By.XPATH, ".//h2[text() = 'Соусы']")  # Текст "Соусы"
    topping_txt = (By.XPATH, ".//h2[text() = 'Начинки']")  # Текст "Начинки"
    bread_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Переход к булкам
    souse_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Переход к соусам
    topping_ul = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Переход к топпингам
    enter_to_acc = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    checkout = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ"


class LoginPageLocators:
    """Форма авторизации"""
    email_place = (By.XPATH, ".//input[@name='name']")  # поле ввода почты
    password_place = (By.XPATH, ".//input[@name='Пароль']")  # поле ввода пароля
    enter_button = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка "Войти"
    registration_button = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")  # ссылка на форму "Зарегистрироваться"
    restore_password_button = (By.XPATH, ".//a[text() = 'Восстановить пароль']")  # ссылка на форму "Восстановить пароль"


class RegistrationPageLocators:
    """Форма регистрации"""
    enter_link = (By.XPATH, ".//a[text() = 'Войти']")
    name_place = (By.XPATH, "(.//input[@name = 'name'])[1]")    # Поле ввода Имя
    email_place = (By.XPATH, "(.//input[@name = 'name'])[2]")   # Поле ввода email
    password_place = (By.XPATH, ".//input[@name = 'Пароль']")   # Поле ввода Пароль
    registration_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    enter_button = (By.XPATH, ".//button[text() = 'Войти']")
    error_message_double_reg = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class ForgotPasswordPlaceLocators:
    """Форма восстановления пароля"""
    email_place = (By.XPATH, ".//input[@name = 'name']")
    restore_button = (By.XPATH, ".//button[text() = 'Восстановить']")
    enter_link = (By.XPATH, ".//a[text() = 'Войти']")
    password_place = (By.XPATH, ".//input[@name = 'Пароль']")
    enter_button = (By.XPATH, ".//button[text() = 'Войти']")
    code_place = (By.XPATH, ".//label[text() ='Введите код из письма']")
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")


class AccountProfile:
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиль
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка история заказов
    exit_button = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    cansel_button = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмена


