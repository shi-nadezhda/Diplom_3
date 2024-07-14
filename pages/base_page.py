import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators import HeaderLocators, ProfilePageLocators
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим вниз до нужного элемента')
    def scroll_to_element(self, locator):     
        element = self.wait_visible_element_on_screen(locator)
        self.wait_visible_element_on_screen(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    
    @allure.step('Ожидаем появление элемента на экране')    
    def wait_visible_element_on_screen(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return (wait.until(expected_conditions.visibility_of_element_located(locator)) and 
                wait.until(expected_conditions.element_to_be_clickable(locator)))


    @allure.step('Проверяем исчезновение или отсутствие элемента на экране')
    def element_not_on_screen(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until_not(expected_conditions.visibility_of_element_located(locator))
    
    
    @allure.step('Ожидаем открытие url')
    def wait_url_opened(self, url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))  
        
        
    @allure.step('Ожидание {sec} секунд по причине: {description}')    
    def waiting(self, sec, description='без причины'):
        time.sleep(sec)
        
    
    @allure.step('Переходим по {url} и ожидаем завершения перехода')
    def get_url(self, url):
        self.driver.get(url)
        self.wait_url_opened(url)
        

    @allure.step('Нажимаем на кнопку Личный кабинет у авторизованного пользователя')
    def click_auth_profile_button(self):
        self.wait_visible_element_on_screen(HeaderLocators.profile_button)
        self.driver.find_element(*HeaderLocators.profile_button).click()
        self.wait_visible_element_on_screen(ProfilePageLocators.exit_button)
    
    
    @allure.step('Нажимаем на кнопку Личный кабинет у неавторизованного пользователя')
    def click_profile_button(self):
        self.wait_visible_element_on_screen(HeaderLocators.profile_button)
        self.driver.find_element(*HeaderLocators.profile_button).click()
        
        
    @allure.step('Нажимаем на кнопку Лента заказов') 
    def click_order_feed(self):
        self.wait_visible_element_on_screen(HeaderLocators.order_feed_button)
        self.driver.find_element(*HeaderLocators.order_feed_button).click()
        
        
    @allure.step('Нажимаем на кнопку Конструктор') 
    def click_constructor_button(self):
        self.wait_visible_element_on_screen(HeaderLocators.constructor_button)
        self.driver.find_element(*HeaderLocators.constructor_button).click()
        
    
    @allure.step('Перетаскиваем элемент')     
    def drag_and_drop(self, sourse_locator, target_locator):
        source_element = self.driver.find_element(*sourse_locator)
        dest_element = self.driver.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
        
        
    @allure.step('Кликаем по элементу')     
    def click_on_element(self, locator):
        self.wait_visible_element_on_screen(locator)
        self.driver.find_element(*locator).click() 
