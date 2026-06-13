from selenium.webdriver.common.by import By

class SigninPageLocators:
    
    EMAIL_SIGNIN_FIELD = By.XPATH, "//input[@type='text']"
    PASSWORD_SIGNIN_FIELD = By.XPATH, "//input[@type='password']"

    SIGNIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//a[text()='Создать аккаунт']"