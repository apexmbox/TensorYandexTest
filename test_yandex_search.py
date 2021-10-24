import pytest
import time
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.images_page import ImagesPage
from pages.search_image_page import SearchImagePage
from urls import YandexUrls


@pytest.mark.yandex_search
class TestYandexTensorSearch:

    @pytest.mark.skip
    def test_yandex_tensor_search(self, browser):
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        main_page.should_be_search_field()
        main_page.should_not_be_suggest_table()
        main_page.complete_search_field_with('тензор')
        main_page.should_be_suggest_table()

        main_page.go_to_search_result_page()

        search_result_page = SearchResultPage(browser, browser.current_url)
        search_result_page.should_be_search_result()
        search_result_page.should_be_results_linked_to('tensor.ru', count=5)

    #@pytest.mark.skip
    def test_yandex_pictures_search(self, browser):
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        main_page.go_to_search_images()

        images_page = ImagesPage(browser, browser.current_url)
        images_page.should_be_images_url()
        images_page.should_be_popular_request_data_grid()

        images_page.go_to_data_grid_item(0)

        search_image_page = SearchImagePage(browser, browser.current_url)
        search_image_page.should_be_search_text_equals(images_page.data_grid_item_text)

        search_image_page.go_to_image(0)
        search_image_page.should_be_full_size_image()
