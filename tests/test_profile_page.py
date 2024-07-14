import allure
from locators import ProfilePageLocators, LoginPageLocators
from data import Urls
from pages.base_page import BasePage
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('Проверка перехода при клике на кнопку "Личный кабинет"')
    @allure.description('При клике на кнопку "Личный кабинет" ожидаем переход в личный кабинет')
    def test_authorise_profile_open_success(self, driver, login):        
        base = BasePage(driver)
        base.click_auth_profile_button()

        assert base.driver.current_url == ProfilePageLocators.url
        
        
    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('При клике на кнопку "История заказов" ожидаем переход в раздел "История заказов"')
    def test_go_order_history_section_success(self, driver, login):
        profile = ProfilePage(driver)
        profile.click_order_history()
        
        assert profile.driver.current_url == Urls.profile_order_history
                
        
    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверяем выход из аккаунта')    
    def test_logout_from_account_success(self, driver, login):
        profile = ProfilePage(driver)
        profile.logout()
        
        assert profile.driver.current_url == Urls.login_url
        assert profile.wait_visible_element_on_screen(LoginPageLocators.login_button)
