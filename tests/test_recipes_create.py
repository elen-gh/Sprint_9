import allure
from pages.main_page import MainPage
from pages.signin_page import SigninPage
from pages.recipes_create_page import RecipesCreatePage
from src.data import ExpectedUrl
from src.helpers import get_recipe_data

class TestRecipesCreate:

    @allure. title("Создание рецепта")
    def test_recipes_create(self, driver, registered_user):
        login_data, password_data = registered_user

        signin_page = SigninPage(driver)
        signin_page.wait_for_new_window_and_check_url(ExpectedUrl.expected_url_signin)
        signin_page.signin(login_data, password_data)

        main_page = MainPage(driver)
        main_page.recipes_create_button_click()

        recipes_create_page = RecipesCreatePage(driver)
        name, ing_one, amount, ing_two, time_val, description, image = get_recipe_data()
        recipes_create_page.recipe_create(name, ing_one, ing_two, amount, time_val, description, image)
        
        recipe_id = recipes_create_page.get_created_recipe_id()
        main_page.recipes_button_click()
        title = main_page.get_first_recipe_title()
        assert title == name

        main_page.first_recipe_card_click()
        main_page.wait_for_url_contains(f"/recipes/{recipe_id}")
        assert recipe_id in driver.current_url
        