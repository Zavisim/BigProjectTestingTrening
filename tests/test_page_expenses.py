import time

from selenium.webdriver.support.select import Select


def test_add_new_expenses(browser, expenses_page, main_page, login_page):
    login_page.login('test', '1234')
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.add_value.click()
    time.sleep(2)
    select = Select(expenses_page.filter_category_expenses)
    select.select_by_visible_text('Продукты')
    time.sleep(2)
    expenses_page.amount_expenses.send_keys('1200')
    time.sleep(2)
    expenses_page.product_description_expenses.send_keys('Ящик пива')
    time.sleep(2)
    expenses_page.save_button_expenses.click()
    time.sleep(2)
    expenses_page.delete_product_description.click()
    time.sleep(2)


def test_filter_month(browser, expenses_page, main_page, login_page):
    login_page.login('test', '1234')
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.filter_month_expenses.click()
    time.sleep(2)
    choice_month = expenses_page.filter_month_expenses
    select = Select(choice_month)
    select.select_by_index(12)
    time.sleep(2)
    select.select_by_index(4)
    time.sleep(2)


