from pages.base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def should_be_search_field(self):
        assert self.is_present_and_visible(*MainPageLocators.SEARCH_FIELD), "Search field is not presented"

    def should_not_be_suggest_table(self):
        assert self.is_not_visible(*MainPageLocators.SEARCH_SUGGEST_TABLE), "Search suggest table is presented, but shouldn't be."

    def should_be_suggest_table(self):
        assert self.is_appeared(*MainPageLocators.SEARCH_SUGGEST_TABLE), "Search suggest table is not presented."

    def should_be_search_button(self):
        assert self.is_present_and_visible(*MainPageLocators.SEARCH_BUTTON), "Search button at started page is not presented."

    def should_be_images_button(self):
        assert self.is_present_and_visible(*MainPageLocators.IMAGES_BUTTON), "Pictures button is not presented."

    def complete_search_field_with(self, text):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(text)

    def go_to_search_result_page(self):
        self.should_be_search_button()
        hover = AC(self.browser).key_down(Keys.ENTER)
        hover.perform()

    def go_to_search_images(self):
        self.should_be_images_button()
        images_item = self.browser.find_element(*MainPageLocators.IMAGES_BUTTON)
        self.url = images_item.get_attribute('href')
        self.open()
