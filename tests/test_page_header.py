import time

from selenium.webdriver import Keys


def test_login(browser, main_page):
    main_page.open()
    main_page.login.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_diagrams(browser, main_page):
    main_page.open()
    main_page.diagrams.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_statistics(browser, main_page):
    main_page.open()
    main_page.statistics.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'statistics'


def test_expenses(browser, main_page):
    main_page.open()
    main_page.expenses.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'expenses'


def test_incomes(browser, main_page):
    main_page.open()
    main_page.incomes.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'incomes'


def test_imports(browser, main_page):
    main_page.open()
    main_page.imports.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'bank-import'


def test_logo(browser, main_page):
    main_page.open()
    main_page.logo.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_page_statistics(browser, statistics_page):
    statistics_page.open()
    statistics_page.table_1_plan.click()
    statistics_page.table_1_plan_input.find().send_keys(Keys.CONTROL, 'a')
    statistics_page.table_1_plan_input.find().send_keys(Keys.DELETE)
    time.sleep(2)
    statistics_page.table_1_plan_input.find().send_keys('1234')
    time.sleep(2)
    statistics_page.table_1_plan_input.find().send_keys(Keys.TAB)
    assert statistics_page.table_1_plan_input.text == '1234'
