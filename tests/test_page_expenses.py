import time

from selenium.webdriver.support.select import Select


def test_add_new_expenses(browser, expenses_page, main_page, login_page):
    login_page.login('test@test.ru', '1234')
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.add_value.click()
    time.sleep(2)
    #expenses_page.choice_category.click()
    choice_category = expenses_page.filter_category
    select = Select(choice_category)
    select.select_by_visible_text('ПРОДУКТЫ')
    time.sleep(2)


def test_filter_month(browser, expenses_page, main_page, login_page):
    login_page.login('test@test.ru', '1234')
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.filter_month.click()
    time.sleep(2)
    choice_month = expenses_page.filter_month
    select = Select(choice_month)
    select.select_by_index(3)
    time.sleep(2)
    select.select_by_index(4)
    time.sleep(2)

