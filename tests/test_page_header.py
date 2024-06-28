import time

from selenium.webdriver import Keys


def test_header_logout_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.logout.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'login'


def test_header_diagrams_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.diagrams.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_header_statistics_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.statistics.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'statistics'


def test_header_expenses_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.expenses.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'expenses'


def test_header_incomes_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.incomes.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'incomes'


def test_header_imports_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.imports.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'bank-import'


def test_header_logo_click_button(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.logo.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_page_statistics_work_cell(browser, statistics_page, main_page):
    statistics_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.statistics.click()
    time.sleep(2)
    statistics_page.table_1_plan.click()
    statistics_page.table_1_plan_input.find().send_keys(Keys.CONTROL, 'a')
    statistics_page.table_1_plan_input.find().send_keys(Keys.DELETE)
    time.sleep(2)
    statistics_page.table_1_plan_input.find().send_keys('1234')
    time.sleep(2)
    statistics_page.table_1_plan_input.find().send_keys(Keys.TAB)
    time.sleep(2)
    assert statistics_page.table_1_plan.find().__getattribute__('text') == '1234'
