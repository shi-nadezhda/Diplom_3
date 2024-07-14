# Тесты для приложения Stellar Burgers
https://stellarburgers.nomoreparties.site/

## Структура
- tests/ - автотесты
    - test_main_functions.py - тесты для проверки общего функционала
    - test_order_feed.py - тесты для проверки раздела ленты заказов
    - test_password_recovery.py - тесты для проверки восстановления пароля
    - test_profile_page.py - тесты для проверки личного кабинета
- conftest.py - фикстуры
- locators/ - локаторы
- user.py - пользователи для заказа
- pages/ - POM
- data.py - файл с данными urls и api

### Запуск тестов: 
`pytest -v --alluredir=allure_results`

### Просмотр отчета
`allure serve allure_results`