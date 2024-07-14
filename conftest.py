import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 
import requests
from locators import LoginPageLocators, BuilderPageLocators
from data import Urls, API
from user import RandomUser
from pages.base_page import BasePage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def get_user():
    payload = RandomUser.fields
    response = requests.post(API.create_user, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(API.delete_user, headers=header)
    
@pytest.fixture
def login(driver, get_user):
    # Авторизация
    base = BasePage(driver)
    base.get_url(LoginPageLocators.url)
    
    user = get_user[0]

    driver.find_element(*LoginPageLocators.email_input).send_keys(user.get('email'))
    driver.find_element(*LoginPageLocators.password_input).send_keys(user.get('password'))
    driver.find_element(*LoginPageLocators.login_button).click()

    WebDriverWait(driver, 20).until(expected_conditions.url_contains(Urls.base_url))
    base.wait_visible_element_on_screen(BuilderPageLocators.checkout_button)
