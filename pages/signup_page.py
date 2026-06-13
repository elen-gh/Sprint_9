from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators
from allure import step


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def signup(self, name, surname, login, email, password):
        with step(f"Signup"):
            self.enter_text(SignupPageLocators.NAME_SIGNUP_FIELD, name)
            self.enter_text(SignupPageLocators.SURNAME_SIGNUP_FIELD, surname)
            self.enter_text(SignupPageLocators.LOGIN_SIGNUP_FIELD, login)
            self.enter_text(SignupPageLocators.EMAIL_SIGNUP_FIELD, email)
            self.enter_text(SignupPageLocators.PASSWORD_SIGNUP_FIELD, password)
            self.click_element(SignupPageLocators.SIGNUP_BUTTON)
    