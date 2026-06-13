from pages.base_page import BasePage
from locators.signin_page_locators import SigninPageLocators
from allure import step


class SigninPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def signin(self, email, password):
        with step(f"Signin"):
            self.enter_text(SigninPageLocators.EMAIL_SIGNIN_FIELD, email)
            self.enter_text(SigninPageLocators.PASSWORD_SIGNIN_FIELD, password)
            self.click_element(SigninPageLocators.SIGNIN_BUTTON)

    @step("Click CREATE_ACCOUNT_BUTTON")
    def create_account_button_click(self):
        self.click_element(SigninPageLocators.CREATE_ACCOUNT_BUTTON)

    def email_signin_field_visible(self):
        element = self.wait_for_element_visible(SigninPageLocators.EMAIL_SIGNIN_FIELD)
        return element
    def password_signin_field_visible(self):
        element = self.wait_for_element_visible(SigninPageLocators.PASSWORD_SIGNIN_FIELD)
        return element
    