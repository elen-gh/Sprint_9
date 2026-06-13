import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
from selenium import webdriver
from src.config import Config
from src.helpers import get_sign_up_data
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


@pytest.fixture
def driver():
    selenoid_url = os.getenv("SELENOID_URL")
    
    if selenoid_url:
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "chrome")
        
        browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        browser = webdriver.Chrome()

    browser.delete_all_cookies()
    browser.get(Config.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user(driver):
    signin_page = SigninPage(driver)
    signin_page.create_account_button_click()

    name_data, surname_data, login_data, email_data, password_data = get_sign_up_data()
    signup_page = SignupPage(driver)
    signup_page.signup(name_data, surname_data, login_data, email_data, password_data)
    
    return login_data, password_data