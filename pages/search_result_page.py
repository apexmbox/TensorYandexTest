from .locators import SearchResultPageLocators
from pages.base_page import BasePage


class SearchResultPage(BasePage):

    def should_be_search_result(self):
        assert self.is_present_and_visible(*SearchResultPageLocators.SEARCH_RESULT), "Search result is not presented."

    def should_be_results_linked_to(self, text_url, count=5):
        for search_result_index in range(count):
            srl_locator = SearchResultPageLocators.generate_locator_for_result(search_result_index)
            found_text_url = self.browser.find_element(*srl_locator).text
            assert found_text_url == text_url,\
                f"Search result №{search_result_index + 1} is not contains '{text_url}', it contains '{found_text_url}'"
