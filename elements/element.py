import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Element:
    def __init__(self, browser: WebDriver, by: By, selector: str):
        self.browser = browser
        self.by = by
        self.selector = selector

    def find(self) -> WebElement:
        return self.browser.find_element(self.by, self.selector)

    def click(self):
        self.find().click()
        logging.info(f'Клик на элемент {self.selector}')

    def send_keys(self, text: str):
        self.find().send_keys(text)
        logging.info(f'Введён текст {text} в {self.selector}')
