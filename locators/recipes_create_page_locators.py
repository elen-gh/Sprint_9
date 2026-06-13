from selenium.webdriver.common.by import By

class RecipesCreatePageLocators:
    RECIPE_NAME_FIELD = By.XPATH, "//div[contains(text(), 'Название рецепта')]/following-sibling::input"

    INGREDIENT_NAME_FIELD = INGREDIENT_INPUT_FIELD = By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]"

    FIRST_DROPDOWN_ITEM = By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div[1]"
    INGREDIENT_AMOUNT_FIELD = By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]"

    INGREDIENT_ADD_BUTTON = By.XPATH, "//div[text()='Добавить ингредиент']"

    RECIPE_TIME_FIELD = By.XPATH, "//div[contains(text(), 'Время приготовления')]/following-sibling::input"
    RECIPE_DESCRIPTION_FIELD = By.CLASS_NAME, "styles_textareaField__1wfhC"

    FILE_INPUT = By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput')]"

    CREATE_RECIPE_BUTTON = By.XPATH, "//button[text()='Создать рецепт']"
