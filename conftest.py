import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.main_page import MainPage
from pages.statistics_page import StatisticsPage


@pytest.fixture
def browser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser) -> MainPage:
    return MainPage(browser)


@pytest.fixture
def statistics_page(browser) -> StatisticsPage:
    return StatisticsPage(browser)
