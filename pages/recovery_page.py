import allure
from locators import LoginPageLocators, ForgotPasswordPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
             
             
    @allure.step('Нажимаем на кнопку восстановить пароль')
    def click_restore_button(self):
        self.wait_visible_element_on_screen(ForgotPasswordPageLocators.restore_button)
        self.driver.find_element(*ForgotPasswordPageLocators.restore_button).click()
        
    
    @allure.step('Нажимаем иконку скрыть / показать пароль')
    def click_password_switch_visible_button(self):
        self.wait_visible_element_on_screen(LoginPageLocators.password_input_hide_button)
        self.driver.find_element(*LoginPageLocators.password_input_hide_button).click()
    