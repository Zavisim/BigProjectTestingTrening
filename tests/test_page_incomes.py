import time

from selenium.webdriver.support.select import Select


def test_page_add_new_incomes(browser, incomes_page, login_page, main_page):
    login_page.login('test', '1234')
    main_page.incomes.click()
    incomes_page.add_income.click()
    time.sleep(2)
    select = Select(incomes_page.filter_category_income)
    select.select_by_visible_text('Зарплата')
    time.sleep(2)
