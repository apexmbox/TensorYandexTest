from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input .input__box .input__control")
    SEARCH_SUGGEST_TABLE = (By.CSS_SELECTOR, ".mini-suggest__popup-content")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button .mini-suggest__button-text")
    IMAGES_BUTTON = (By.CSS_SELECTOR, "[data-id='images']")


class SearchResultPageLocators:
    SEARCH_RESULT = (By.CSS_SELECTOR, "#search-result")

    @staticmethod
    def generate_locator_for_result(index):
        return By.CSS_SELECTOR, f"#search-result li[data-cid='{index}'] .path b"


class ImagesPageLocators:
    POPULAR_REQUEST_DATA_GRID = (By.CSS_SELECTOR, "div.PopularRequestList")
    DATA_GRID_FIRST_ITEM = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    DATA_GRID_FIRST_ITEM_SEARCH_TEXT = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")

    DATA_GRID_ITEM_TEXT_ATTRIBUTE = "data-grid-text"

    @staticmethod
    def generate_locator_for_data_grid_item(index):
        return By.CSS_SELECTOR, f".PopularRequestList-Item_pos_{index}"

    @staticmethod
    def generate_locator_for_data_grid_item_link(index):
        return By.CSS_SELECTOR, f".PopularRequestList-Item_pos_{index} a"


class SearchImagePageLocators:
    SEARCH_FIELD_CLASS_TEXT_ATTRIBUTE = 'input__control'
    FULL_SIZE_IMAGE = (By.CSS_SELECTOR, ".MMImageContainer .MMImage-Preview")
    NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    PREV_IMAGE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")

    @staticmethod
    def generate_locator_for_image(index):
        return By.CSS_SELECTOR, f".serp-list .serp-item_pos_{index}"

    @staticmethod
    def generate_locator_for_image_link(index):
        return By.CSS_SELECTOR, f".serp-list .serp-item_pos_{index} a"
