import time


def test_correct_authorization(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_incorrect_authorization_password(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1235')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'login'


def test_incorrect_authorization_username(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('pykpyk@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'login'
