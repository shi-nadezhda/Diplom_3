import allure
from locators import BuilderPageLocators
from data import Urls
from pages.base_page import BasePage
from pages.builder_page import BuilderPage


class TestMainFunctions:
    @allure.title('Проверка перехода при клике на кнопку "Конструктор"')
    @allure.description('При клике на кнопку "Конструктор" ожидаем переход в Конструктор')
    def test_switch_to_constructor_success(self, driver, login):
        base = BasePage(driver)
        base.get_url(Urls.base_url)
        base.click_constructor_button()
    
        assert base.driver.current_url == Urls.base_url
        

    @allure.title('Проверка перехода при клике на кнопку "Лента заказов"')
    @allure.description('При клике на кнопку "Лента заказов" ожидаем переход в Ленту заказов')
    def test_go_order_history_section_success(self, driver):
        base = BasePage(driver)
        base.get_url(Urls.base_url)
        base.click_order_feed()
        
        assert base.driver.current_url == Urls.order_feed
        
       
    @allure.title('Проверка всплывающего окна ингредиентов')
    @allure.description('При клике на ингредиент ожидаем высплывающее окно с деталями. Окно можно закрыть кликом по крестику') 
    def test_clicking_on_ingredient_opens_window_with_details_success(self, driver):
        constructor = BuilderPage(driver)
        constructor.get_url(Urls.base_url)
        constructor.click_ingredient_card()
        
        assert constructor.wait_visible_element_on_screen(BuilderPageLocators.ingredient_modal)
        
        constructor.close_ingredient_modal()
        
        assert constructor.element_not_on_screen(BuilderPageLocators.ingredient_modal)
        
    
    @allure.title('Проверка счетчика ингредиента')
    @allure.description('При добавлении ингредиента ожидаем увеличение счетчика')   
    def test_counter_increases_when_adding_ingredient_to_order_success(self, driver):
        constructor = BuilderPage(driver)
        constructor.get_url(Urls.base_url)
        constructor.wait_visible_element_on_screen(BuilderPageLocators.ingredient_card_counter)
        
        assert constructor.driver.find_element(*BuilderPageLocators.ingredient_card_counter).text == "0"
        
        constructor.dnd_ingredient_to_basket()
        
        assert constructor.driver.find_element(*BuilderPageLocators.ingredient_card_counter).text == "2"
        
        
    @allure.title('Проверка оформления заказа')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_logged_user_can_place_order_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.get_url(Urls.base_url)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        
        assert constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
