import time


def test_add_new_expenses(browser, expenses_page, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.add_value.click()
    time.sleep(2)
    expenses_page.choice_category.click()
    time.sleep(2)


def test_filter_month(browser, expenses_page, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    main_page.expenses.click()
    time.sleep(2)
    expenses_page.filter_month.click()
    time.sleep(2)

