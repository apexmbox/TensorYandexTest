from pages.base_page import BasePage
from .locators import SearchImagePageLocators


class SearchImagePage(BasePage):
    def should_be_search_text_equals(self, text):
        search_text = self.browser.execute_script(f"return document.getElementsByClassName('\
            {SearchImagePageLocators.SEARCH_FIELD_CLASS_TEXT_ATTRIBUTE}').text.value")
        assert search_text == text, "Search text not equals data grid item text."

    def should_be_image(self, image_index):
        assert self.is_present_and_visible(*SearchImagePageLocators.generate_locator_for_image(image_index)),\
            f"Image №{image_index} is not presented."

    def should_be_full_size_image(self):
        assert self.is_present_and_visible(*SearchImagePageLocators.FULL_SIZE_IMAGE),\
            "Full size image is not presented."

    def go_to_image(self, image_index):
        self.should_be_image(image_index)
        image_link = self.browser.find_element(*SearchImagePageLocators.generate_locator_for_image_link(image_index))
        self.url = image_link.get_attribute('href')
        self.open()
