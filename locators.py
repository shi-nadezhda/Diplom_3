from selenium.webdriver.common.by import By
from data import Urls
    
class HeaderLocators:
    """Шапка страницы"""
    page_title_button = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # заголовок страницы
    constructor_button = (By.XPATH, ".//p[text()='Конструктор']") # кнопка "Конструктор"
    order_feed_button = (By.XPATH, ".//p[text()='Лента Заказов']") # кнопка "Лента заказов"
    profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']") # кнопка "Личный кабинет"
    
class FeedLocators:
    """Страница ленты заказов"""
    feed_orders_id = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]//p[contains(@class, 'text_type_digits-default')]") # id заказа в ленте заказов
    feed_orders_counter = (By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'OrderFeed_number')]") # счетчик за все время
    feed_orders_counter_today = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[contains(@class, 'OrderFeed_number')]") # счетчик за сегодня
    order_in_progress = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text')]") # заказ в работе

class BuilderPageLocators:
    """Страница с конструктором"""
    url = Urls.base_url
    buns_tab = (By.XPATH, ".//span[text()='Булки']") # Раздел "Булки"
    sauce_tab = (By.XPATH, ".//span[text()='Соусы']") # Раздел "Соусы"
    filling_tab = (By.XPATH, ".//span[text()='Начинки']") # Раздел "Начинки"
    current_tab = (By.XPATH, ".//div[contains(@class, 'tab_tab') and contains(@class, 'current')]/span") # активная вкладка
    login_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    checkout_button = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка "Оформить заказ"
    ingredient_card = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")  # ингредиент
    ingredient_modal = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]") # модальное окно ингредиента
    ingredient_modal_close_button = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]") # кнопка закрытия "Крестик" на модальном окне ингридиентов
    constructor_basket = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]") # корзина конструктора
    ingredient_card_counter = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]") # счетчик на карточке ингредиента
    order_text_complete = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]//*[text()='Ваш заказ начали готовить']") # окно Ваш заказ начали готовить
    order_complete_close_button = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]") # кнопка закрытия "Крестик" на модальном окне принятого заказа
    order_complete_id = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]//*[contains(@class, 'Modal_modal__title')]")

class RegisterPageLocators:
    """Форма регистрации"""
    url = Urls.register_url
    name_input = (By.XPATH, ".//label[text()='Имя']/parent::*//input") # поле ввода имени
    email_input = (By.XPATH, ".//label[text()='Email']/parent::*//input") # поле ввода email
    password_input = (By.XPATH, ".//label[text()='Пароль']/parent::*//input") # поле ввода пароля
    register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться"
    error_incorrect_password = (By.XPATH, ".//p[text()='Некорректный пароль']") # ошибка для некорректного пароля
    login_link = (By.XPATH, ".//a[text()='Войти']") # ссылка "Войти"
        
class LoginPageLocators:    
    """Форма входа"""
    url = Urls.login_url
    email_input = (By.XPATH, ".//label[text()='Email']/parent::*//input") # поле ввода email
    password_input = (By.XPATH, ".//label[text()='Пароль']/parent::*//input") # поле ввода пароля
    password_input_active = (By.XPATH, ".//label[text()='Пароль']/parent::*[contains(@class, 'input_status_active')]//input") # поле ввода пароля
    password_input_hide_button = (By.XPATH, ".//label[text()='Пароль']/parent::*//div[contains(@class, 'input__icon-action')]") # кнопка скрыть/ показать пароль
    login_button = (By.XPATH, ".//button[text()='Войти']") # кнопка "Войти"
    register_link = (By.XPATH, ".//a[text()='Зарегистрироваться']") # ссылка "Зарегистрироваться"
    restore_password_link = (By.XPATH, ".//a[text()='Восстановить пароль']") # ссылка "Восстановить пароль"
    
class ProfilePageLocators:
    """Личный кабинет"""
    url = Urls.profile_url   
    exit_button = (By.XPATH, ".//button[text()='Выход']") # кнопка "Выход"
    order_history_button = (By.XPATH, ".//a[text()='История заказов']") # кнопка "История заказов"
    order_history_item_name = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]//h2") # название элемента истории заказов
    order_history_item_modal_name = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//h2") # название в окне подробной информации о заказе
    
class ForgotPasswordPageLocators:
    """Страница восстановления пароля"""
    url = Urls.forgot_password_url
    login_link = (By.XPATH, ".//a[text()='Войти']") # ссылка "Войти"
    email_input = (By.XPATH, ".//label[text()='Email']/parent::*//input") # поле ввода email
    restore_button = (By.XPATH, ".//button[text()='Восстановить']") # кнопка "Восстановить"
    reset_password_title = (By.XPATH, ".//h2[text()='Восстановление пароля']") # заголовок формы восстановления пароля
    