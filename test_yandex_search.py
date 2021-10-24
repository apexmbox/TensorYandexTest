import pytest
import time
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.images_page import ImagesPage
from pages.search_image_page import SearchImagePage
from urls import YandexUrls


@pytest.mark.yandex_search
class TestYandexTensorSearch:

    # Тестовый сценарий №1
    @pytest.mark.xfail(reason="First five results can't contain only one site link.")
    def test_yandex_tensor_search(self, browser):
        # 1. Зайти на yandex.ru
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        # 2. Проверить наличие поля поиска
        main_page.should_be_search_field()

        # 3. Ввести в поиск "Тензор"
        main_page.complete_search_field_with('Тензор')

        # 4. Проверить, что появилась таблица с подсказками
        main_page.should_be_suggest_table()

        # 5. При нажатии на Enter появляется таблица результатов поиска
        main_page.go_to_search_result_page()

        search_result_page = SearchResultPage(browser, browser.current_url)
        search_result_page.should_be_search_result()

        # 6. В первых пяти результатах есть ссылка на tensor.ru
        search_result_page.should_be_results_linked_to('tensor.ru', count=5)

    # Тестовый сценарий №2
    def test_yandex_pictures_search(self, browser):
        # 1. Зайти на yandex.ru
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        # 2. Ссылка "Картинки" присутствует на странице
        main_page.should_be_images_button()

        # 3. Кликаем на ссылку
        main_page.go_to_search_images()
        images_page = ImagesPage(browser, browser.current_url)

        # 4. Проверить, что перешли на нужный url
        images_page.should_be_images_url()
        images_page.should_be_popular_request_data_grid()

        # 5. Открыть 1 категорию, проверить, что открылась, в поиске верный текст
        images_page.go_to_data_grid_item(0)

        search_image_page = SearchImagePage(browser, browser.current_url)
        search_image_page.should_be_search_text_equals(images_page.data_grid_item_text)

        # 6. Открыть 1 картинку, проверить, что открылась
        search_image_page.go_to_image(0)
        search_image_page.should_be_full_size_image()
        time.sleep(1)

        # 7. При нажатии кнопки вперед картинка изменяется
        search_image_page.should_be_another_image_by_next_click()
        time.sleep(1)

        # 8. При нажатии кнопки назад картинка изменяется на изображение из шага 6.
        search_image_page.should_be_same_prev_image_by_prev_click()
        time.sleep(1)
