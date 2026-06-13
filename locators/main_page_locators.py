from selenium.webdriver.common.by import By

class MainPageLocators:
    EXIT_BUTTON = By.XPATH, "//a[text()='Выход']"
    RECIPES_CREATE_BUTTON = By.XPATH, "//a[text()='Создать рецепт']"

    RECIPES_BUTTON = By.XPATH, "//a[text()='Рецепты']"

    FIRST_RECIPE_CARD = By.XPATH, "(//div[contains(@class, 'style_card__')]//a[contains(@class, 'style_card__title')])[2]"
    FIRST_RECIPE_CARD_TITLE = By.XPATH, "(//div[contains(@class, 'style_card__')]//a[contains(@class, 'style_card__title')])[2]"