class Urls:
    """URL"""
    base_url = "https://stellarburgers.nomoreparties.site/" # главная страница
    login_url = base_url + "login" # логин пользователя
    register_url = base_url + "register" # создать пользователя
    forgot_password_url = base_url + "forgot-password" # восстановить пароль
    profile_url = base_url + "account/profile" # личный кабинет
    profile_order_history = base_url + "account/order-history" # получить заказы конкретного пользователя
    order_feed = base_url + "feed" # лента заказов
    reset_password = base_url + "reset-password" # ввод нового пароля для восстановления доступа

class API:
    create_user = Urls.base_url + "api/auth/register"
    delete_user = Urls.base_url + "api/auth/user"