import time

from selenium.webdriver import Keys


def test_page_header(browser, main_page):
    main_page.open()
    main_page.login.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL
    main_page.diagrams.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL
    main_page.statistics.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'statistics'
    main_page.expenses.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'expenses'
    main_page.incomes.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'incomes'
    main_page.imports.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'bank-import'
    main_page.logo.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_page_statistics(browser, statistics_page):
    statistics_page.open()
    statistics_page.table_1_plan.click()
    statistics_page.table_1_plan_input.find().clear()
    statistics_page.table_1_plan_input.send_keys('1234')
    time.sleep(5)
