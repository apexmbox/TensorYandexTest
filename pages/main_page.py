import pytest
from pages.base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):

    def should_be_search_field(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_FIELD), "Search field is not presented"

    @pytest.mark.parametrize('search_text', )
    def