from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from allure import step


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def exit_button_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.EXIT_BUTTON)
        return element
    
    @step("Click RECIPES_CREATE_BUTTON")
    def recipes_create_button_click(self):
        self.click_element(MainPageLocators.RECIPES_CREATE_BUTTON)

    @step("Click RECIPES_BUTTON")
    def recipes_button_click(self):
        self.click_element(MainPageLocators.RECIPES_BUTTON)

    @step("Click FIRST_RECIPE_CARD")
    def first_recipe_card_click(self):
        self.click_element(MainPageLocators.FIRST_RECIPE_CARD)

    def get_first_recipe_title(self):
        with step("GET_RECIPE_TITLE"):
            element = self.wait_for_element_visible(MainPageLocators.FIRST_RECIPE_CARD_TITLE)
            return element.text
