from pages.base_page import BasePage
from .locators import ImagesPageLocators
from urls import YandexUrls


class ImagesPage(BasePage):

    data_grid_item_text = ''

    def should_be_images_url(self):
        assert YandexUrls.YANDEX_IMAGES_URL in self.browser.current_url, \
            f"Current URL is not '{YandexUrls.YANDEX_IMAGES_URL}"

    def should_be_popular_request_data_grid(self):
        assert self.is_present_and_visible(*ImagesPageLocators.POPULAR_REQUEST_DATA_GRID),\
            "Popular request data grid is not presented."

    def should_be_data_grid_item(self, item_index):
        assert self.is_present_and_visible(*ImagesPageLocators.generate_locator_for_data_grid_item(item_index)),\
            f"Data grid item №{item_index} is not presented."

    def get_data_grid_item_text(self, item_index):
        self.should_be_data_grid_item(item_index)
        item = self.browser.find_element(*ImagesPageLocators.generate_locator_for_data_grid_item(item_index))
        return item.get_attribute(ImagesPageLocators.DATA_GRID_ITEM_TEXT_ATTRIBUTE)

    def go_to_data_grid_item(self, item_index):
        self.should_be_data_grid_item(item_index)
        self.data_grid_item_text = self.get_data_grid_item_text(item_index)
        dg_item_link = self.browser.find_element(*ImagesPageLocators.generate_locator_for_data_grid_item_link(item_index))
        self.url = dg_item_link.get_attribute('href')
        self.open()
