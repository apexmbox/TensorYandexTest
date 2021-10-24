from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input .input__box")
