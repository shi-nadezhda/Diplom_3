import allure
from locators import LoginPageLocators, BuilderPageLocators
from data import Urls
from pages.base_page import BasePage


class BuilderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    @allure.step('Нажимаем на ингридиент') 
    def click_ingredient_card(self):
        self.click_on_element(BuilderPageLocators.ingredient_card)
        
    
    @allure.step('Закрываем модальное окно ингридиента')
    def close_ingredient_modal(self):
        self.click_on_element(BuilderPageLocators.ingredient_modal_close_button) 
        
        
    @allure.step('Перетаскиваем ингредиент в корзину')    
    def dnd_ingredient_to_basket(self): 
        self.wait_visible_element_on_screen(BuilderPageLocators.ingredient_card)
        self.wait_visible_element_on_screen(BuilderPageLocators.constructor_basket)
        self.drag_and_drop(BuilderPageLocators.ingredient_card, BuilderPageLocators.constructor_basket)
        
        
    @allure.step('Нажимаем на кнопку "Оформить заказ"') 
    def click_checkout_button(self):
        self.click_on_element(BuilderPageLocators.checkout_button)
        
        
    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_restore_password_link(self):
        self.wait_visible_element_on_screen(LoginPageLocators.restore_password_link)
        self.driver.find_element(*LoginPageLocators.restore_password_link).click()
        self.wait_url_opened(Urls.forgot_password_url)
        
        
    @allure.step('Закрываем модальное окно принятия заказа')
    def close_order_complete_modal(self):
        self.click_on_element(BuilderPageLocators.order_complete_close_button) 
