from pages.base_page import BasePage
from locators.recipes_create_page_locators import RecipesCreatePageLocators
from allure import step


class RecipesCreatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def recipe_create(self, name, ingredient_one, ingredient_two, amount, time, description, image):
        with step(f"Signin"):
            self.enter_text(RecipesCreatePageLocators.RECIPE_NAME_FIELD, name)

            self.select_from_dropdown(
                input_locator=RecipesCreatePageLocators.INGREDIENT_NAME_FIELD,
                text_to_type=ingredient_one,
                first_item_locator=RecipesCreatePageLocators.FIRST_DROPDOWN_ITEM
            )
            
            self.enter_text(RecipesCreatePageLocators.INGREDIENT_AMOUNT_FIELD, str(amount))
            
            self.click_element(RecipesCreatePageLocators.INGREDIENT_ADD_BUTTON)
            self.select_from_dropdown(
                input_locator=RecipesCreatePageLocators.INGREDIENT_NAME_FIELD, text_to_type=ingredient_two,
                first_item_locator=RecipesCreatePageLocators.FIRST_DROPDOWN_ITEM
            )
            self.enter_text(RecipesCreatePageLocators.INGREDIENT_AMOUNT_FIELD, str(amount))
            
            self.click_element(RecipesCreatePageLocators.INGREDIENT_ADD_BUTTON)

            self.enter_text(RecipesCreatePageLocators.RECIPE_TIME_FIELD, str(time))
            self.enter_text(RecipesCreatePageLocators.RECIPE_DESCRIPTION_FIELD, description)

            file_field = self.driver.find_element(*RecipesCreatePageLocators.FILE_INPUT)
            file_field.send_keys(image)

            self.click_element(RecipesCreatePageLocators.CREATE_RECIPE_BUTTON)

    def get_created_recipe_id(self):
        self.wait_for_url_matches(r".*/recipes/\d+/?$")
        current_url = self.driver.current_url
        recipe_id = current_url.rstrip('/').split('/')[-1]
        return recipe_id
    