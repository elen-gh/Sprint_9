import allure
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from src.data import ExpectedUrl
from src.helpers import get_sign_up_data

class TestSignup:

    @allure. title("Создание аккаунта")
    def test_signup(self, driver):

        signin_page = SigninPage(driver)
        signin_page.create_account_button_click()
    
        name_data, surname_data, login_data, email_data, password_data = get_sign_up_data()
        signup_page = SignupPage(driver)
        signup_page.signup(name_data, surname_data, login_data, email_data, password_data)

        current_url = signin_page.wait_for_new_window_and_check_url(ExpectedUrl.expected_url_signin)
        
        assert "signin" in current_url
        assert signin_page.email_signin_field_visible()
        assert signin_page.password_signin_field_visible()