import math
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser: WebDriver = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_present_and_visible(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            if element.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def is_not_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_appeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_not_visible(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            if element.is_displayed():
                return False
            else:
                return True
        except NoSuchElementException:
            return True
