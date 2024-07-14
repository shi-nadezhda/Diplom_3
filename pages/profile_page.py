import allure
from locators import ProfilePageLocators
from data import Urls
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
             
             
    @allure.step('Нажимаем на кнопку История заказов')
    def click_order_history(self):
        self.click_auth_profile_button()
        self.wait_visible_element_on_screen(ProfilePageLocators.order_history_button)
        self.driver.find_element(*ProfilePageLocators.order_history_button).click()
        self.wait_url_opened(Urls.profile_order_history)
        
        
    @allure.step('Выходим из аккаунта')    
    def logout(self):
        self.click_auth_profile_button()
        self.wait_visible_element_on_screen(ProfilePageLocators.exit_button)
        self.driver.find_element(*ProfilePageLocators.exit_button).click()
        self.wait_url_opened(Urls.login_url)   
  