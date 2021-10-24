from pages.base_page import BasePage
from .locators import SearchImagePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchImagePage(BasePage):

    next_image_src = ''
    prev_image_src = ''

    def should_be_search_text_equals(self, text):
        search_text = self.browser.execute_script(f"return document.getElementsByClassName('\
            {SearchImagePageLocators.SEARCH_FIELD_CLASS_TEXT_ATTRIBUTE}').text.value;")
        assert search_text == text, "Search text not equals data grid item text."

    def should_be_image(self, image_index):
        assert self.is_present_and_visible(*SearchImagePageLocators.generate_locator_for_image(image_index)),\
            f"Image №{image_index} is not presented."

    def should_be_full_size_image(self):
        assert self.is_present_and_visible(*SearchImagePageLocators.FULL_SIZE_IMAGE),\
            "Full size image is not presented."

    def should_be_another_image_by_next_click(self):
        self.go_to_next_image()
        assert self.prev_image_src != self.get_current_image_src(), "Should be another image by next click, but it's same."

    def should_be_same_prev_image_by_prev_click(self):
        self.go_to_prev_image()
        assert self.prev_image_src == self.get_current_image_src(), "Should be same image by prev click, but it's another."

    def get_current_image_src(self):
        image = self.browser.find_element(*SearchImagePageLocators.FULL_SIZE_IMAGE)
        return image.get_attribute('src')

    def go_to_image(self, image_index):
        self.should_be_image(image_index)
        image_link = self.browser.find_element(*SearchImagePageLocators.generate_locator_for_image_link(image_index))
        self.url = image_link.get_attribute('href')
        self.open()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(SearchImagePageLocators.FULL_SIZE_IMAGE)
        )

    def go_to_next_image(self):
        self.prev_image_src = self.get_current_image_src()
        next_button = self.browser.find_element(*SearchImagePageLocators.NEXT_IMAGE_BUTTON)
        next_button.click()

    def go_to_prev_image(self):
        self.next_image_src = self.get_current_image_src()
        prev_button = self.browser.find_element(*SearchImagePageLocators.PREV_IMAGE_BUTTON)
        prev_button.click()
