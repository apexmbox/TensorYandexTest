import pytest
from pages.main_page import MainPage
from urls import YandexUrls


@pytest.mark.yandex_search
class TestYandexTensorSearch:
    def test_yandex_tensor_search(self, browser):
        main_page = MainPage(browser, YandexUrls.YANDEX_MAIN_URL)
        main_page.open()

        main_page.should_be_search_field()


@pytest.mark.login_from_main_page
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_see_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_not_be_basket_items()
    basket.should_be_empty_basket_message()
