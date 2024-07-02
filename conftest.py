import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.expenses_page import ExpensesPage
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


# TODO тут ты видимо хотел передать авторизацию в фикстуры страниц
#  чтобы авторизация происходила до теста, но перепутал,
#  надо наоборот передавать authorization в фикстуры страниц
@pytest.fixture
def authorization(browser, main_page, statistics_page):
    # TODO нет перехода на страницу, уже писал в другом месте, тут надо использовать не MainPage
    #  а сделать новый PageObject LoginPage
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()