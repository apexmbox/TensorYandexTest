import pytest
import time
from pages.main_page import MainPage
from urls import YandexUrls


@pytest.mark.yandex_search
class TestYandexTensorSearch:
    def test_yandex_tensor_search(self, browser):
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        main_page.should_be_search_field()
        main_page.should_not_be_suggest_table()
        main_page.complete_search_field_with('тензор')
        main_page.should_be_suggest_table()

        main_page.go_to_search_results()
        time.sleep(5)
