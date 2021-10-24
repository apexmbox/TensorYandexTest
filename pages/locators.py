from selenium.webdriver.common.by import By


class BasePageLocators:
    pass

class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input .input__box .input__control")
    SEARCH_SUGGEST_TABLE = (By.CSS_SELECTOR, ".mini-suggest__popup-content")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button .mini-suggest__button-text")
