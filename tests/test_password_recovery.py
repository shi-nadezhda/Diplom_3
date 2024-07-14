import allure
from locators import LoginPageLocators, ForgotPasswordPageLocators
from data import Urls
from user import User
from pages.builder_page import BuilderPage
from pages.recovery_page import RecoveryPage


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('При клике на кнопку "Восстановить пароль" ожидаем переход а страницу восстановления пароля')  
    def test_go_password_recovery_page_success(self, driver):
        base = BuilderPage(driver)
        base.get_url(Urls.base_url)
        base.click_profile_button()
        base.click_restore_password_link()
        
        assert base.driver.current_url == Urls.forgot_password_url
          

    @allure.title('Проверка ввода почты на странице восстановления')
    @allure.description('Проверяем ввод почты на странице восстановления и клик по кнопке "Восстановить"')         
    def test_entering_mail_success(self, driver):
        recovery = RecoveryPage(driver)
        recovery.get_url(Urls.forgot_password_url)
        recovery.driver.find_element(*ForgotPasswordPageLocators.email_input).send_keys(User.email)
        recovery.click_restore_button()
        
        assert recovery.wait_visible_element_on_screen(ForgotPasswordPageLocators.reset_password_title)
        

    @allure.title('Проверка кнопки "Показать/Скрыть пароль"')
    @allure.description('При клике на кнопку "Показать/Скрыть пароль" ожидаем активацию поля (подсвечивание)')         
    def test_clicking_show_hide_password_button_makes_field_active_success(self, driver):
        recovery = RecoveryPage(driver)
        recovery.get_url(Urls.login_url)
        recovery.wait_visible_element_on_screen(LoginPageLocators.password_input)
        assert recovery.element_not_on_screen(LoginPageLocators.password_input_active)

        recovery.click_password_switch_visible_button()

        assert recovery.wait_visible_element_on_screen(LoginPageLocators.password_input_active)
