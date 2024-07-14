import allure
from locators import ProfilePageLocators, BuilderPageLocators, FeedLocators
from data import Urls
from pages.profile_page import ProfilePage
from pages.builder_page import BuilderPage
from pages.profile_page import ProfilePage


class TestOrderfeed:
    @allure.title('Проверка всплывающего окна заказа')
    @allure.description('При клике на заказ ожидаем высплывающее окно с деталями заказа')
    def test_clicking_on_order_opens_order_details_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
        constructor.close_order_complete_modal()
        
        profile = ProfilePage(driver)
        profile.click_auth_profile_button()
        profile.click_order_history()
        profile.wait_visible_element_on_screen(ProfilePageLocators.order_history_item_name)
        profile.click_on_element(ProfilePageLocators.order_history_item_name)
        
        assert profile.wait_visible_element_on_screen(ProfilePageLocators.order_history_item_modal_name)
        assert profile.driver.find_element(*ProfilePageLocators.order_history_item_name).text == profile.driver.find_element(*ProfilePageLocators.order_history_item_modal_name).text
        
        
    @allure.title('Проверка отображения заказов пользователя на странице "Лента заказов"')
    @allure.description('Проверяем отображение заказов пользователя из раздела "История заказов" на странице "Лента заказов"')    
    def test_user_orders_are_displayed_in_order_feed_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
        constructor.waiting(3, "Ожидание формирования ID заказа")
        order_id = constructor.driver.find_element(*BuilderPageLocators.order_complete_id).text
        constructor.close_order_complete_modal()
        constructor.click_order_feed()
        constructor.wait_visible_element_on_screen(FeedLocators.feed_orders_id)
        feed_order_id = constructor.driver.find_element(*FeedLocators.feed_orders_id).text
        
        assert order_id in feed_order_id
        
    
    @allure.title('Проверка счетчика "Выполнено" за все время')
    @allure.description('При создании заказа ожидаем увеличение счетчика "Выполнено" за все время')     
    def test_increasing_counter_for_all_time_when_creating_an_order_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.get_url(Urls.order_feed)
        constructor.wait_visible_element_on_screen(FeedLocators.feed_orders_counter)
        start_count = constructor.driver.find_element(*FeedLocators.feed_orders_counter).text
        
        constructor.get_url(Urls.base_url)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
        
        constructor.get_url(Urls.order_feed)
        constructor.wait_visible_element_on_screen(FeedLocators.feed_orders_counter)
        end_count = constructor.driver.find_element(*FeedLocators.feed_orders_counter).text
        
        assert int(start_count) == int(end_count) - 1
        
     
    @allure.title('Проверка счетчика "Выполнено" за сегодня')
    @allure.description('При создании заказа ожидаем увеличение счетчика "Выполнено" за сегодня')          
    def test_increasing_counter_for_today_when_creating_an_order_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.get_url(Urls.order_feed)
        constructor.wait_visible_element_on_screen(FeedLocators.feed_orders_counter_today)
        start_count = constructor.driver.find_element(*FeedLocators.feed_orders_counter_today).text
        
        constructor.get_url(Urls.base_url)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
        
        constructor.get_url(Urls.order_feed)
        constructor.wait_visible_element_on_screen(FeedLocators.feed_orders_counter_today)
        end_count = constructor.driver.find_element(*FeedLocators.feed_orders_counter_today).text
        
        assert int(start_count) == int(end_count) - 1
        

    @allure.title('Проверка номера заказа в разделе "В работе"')
    @allure.description('При оформении заказа ожидаем его номер в разделе "В работе"')          
    def test_order_number_appears_in_work_in_progress_section_success(self, driver, login):
        constructor = BuilderPage(driver)
        constructor.dnd_ingredient_to_basket()
        constructor.click_checkout_button()
        constructor.wait_visible_element_on_screen(BuilderPageLocators.order_text_complete)
        constructor.waiting(3, "Ожидание формирования ID заказа")
        order_id = constructor.driver.find_element(*BuilderPageLocators.order_complete_id).text
        
        constructor.get_url(Urls.order_feed)

        constructor.wait_visible_element_on_screen(FeedLocators.order_in_progress)

        constructor.waiting(5, "Ожидание добавления ID заказа в раздел В работе")
        order_in_progress_id = constructor.driver.find_element(*FeedLocators.order_in_progress).text
        
        assert order_id in order_in_progress_id
