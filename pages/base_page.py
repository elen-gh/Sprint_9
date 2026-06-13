from allure import step
from src.config import Config
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver 


class BasePage:
    TIMEOUT = Config.TIMEOUT 
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, timeout=TIMEOUT):
        with step(f"Find element {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        
    def click_element(self, locator, timeout=TIMEOUT):
        with step(f"Click to {locator}"):
            button = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", button)        
    
    def enter_text(self, locator, text, timeout=TIMEOUT):
        with step(f"Fill text {text} into field with locator {locator}"):
            field = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", field) 
            field.send_keys(text)

    def wait_for_element_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def wait_for_url_contains(self, url_part, timeout=TIMEOUT):
        with step(f"Wait for URL: {url_part}"):
            return WebDriverWait(self.driver, timeout).until(lambda driver: url_part in driver.current_url)
       
    def wait_for_new_window_and_check_url(self, expected_url_part):
        with step(f"Check URL: {expected_url_part}"):
            self.wait_for_url_contains(expected_url_part)
            return self.driver.current_url 

    def select_from_dropdown(self, input_locator, text_to_type, first_item_locator):
        self.enter_text(input_locator, text_to_type)
        self.wait_for_element_visible(first_item_locator)
        first_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(first_item_locator))
        first_item.click()

    def wait_for_url_matches(self, pattern, timeout=TIMEOUT):
        with step(f"Ожидание соответствия URL шаблону: {pattern}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.url_matches(pattern)
            )

    