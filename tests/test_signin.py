import allure
from pages.main_page import MainPage
from pages.signin_page import SigninPage  
from src.data import ExpectedUrl

class TestSignin:

    @allure. title("Авторизация")
    def test_signin(self, driver, registered_user):
        login_data, password_data = registered_user

        signin_page = SigninPage(driver)
        signin_page.wait_for_new_window_and_check_url(ExpectedUrl.expected_url_signin)
        signin_page.signin(login_data, password_data)
    
        main_page = MainPage(driver)
        current_url = main_page.wait_for_new_window_and_check_url(ExpectedUrl.expected_url_recipes)
        
        assert "recipes" in current_url
        assert main_page.exit_button_visible()