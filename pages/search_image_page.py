from pages.base_page import BasePage
from .locators import SearchImagePageLocators


class SearchImagePage(BasePage):
    def should_be_search_text_equals(self, text):
        search_text = self.browser.execute_script(f"return document.getElementsByClassName('\
            {SearchImagePageLocators.SEARCH_FIELD_CLASS_TEXT_ATTRIBUTE}').text.value")
        assert search_text == text, "Search text not equals data grid item text."
