from selenium.webdriver.common.by import By

class SignupPageLocators:
    NAME_SIGNUP_FIELD = By.XPATH, "//input[@name='first_name']"
    SURNAME_SIGNUP_FIELD = By.XPATH, "//input[@name='last_name']"
    LOGIN_SIGNUP_FIELD = By.XPATH, "//input[@name='username']"
    EMAIL_SIGNUP_FIELD = By.XPATH, "//input[@name='email']"
    PASSWORD_SIGNUP_FIELD = By.XPATH, "//input[@type='password']"

    SIGNUP_BUTTON = By.XPATH, "//button[text()='Создать аккаунт']"