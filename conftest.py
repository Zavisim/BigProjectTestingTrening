import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.expenses_page import ExpensesPage
from pages.login_page import LoginPage
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


@pytest.fixture
def expenses_page(browser) -> ExpensesPage:
    return ExpensesPage(browser)


@pytest.fixture
def login_page(browser) -> LoginPage:
    return LoginPage(browser)
