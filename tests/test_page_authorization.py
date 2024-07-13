import time


def test_correct_authorization(browser, login_page, main_page):
    login_page.login('test@test.ru', '1234')
    assert browser.current_url == main_page.URL


def test_incorrect_password_authorization(browser, login_page):
    login_page.login('test@test.ru', '1235')
    assert browser.current_url == login_page.URL


def test_incorrect_username_authorization(browser, login_page):
    login_page.login('pykpyk@test.ru', '1234')
    assert browser.current_url == login_page.URL
