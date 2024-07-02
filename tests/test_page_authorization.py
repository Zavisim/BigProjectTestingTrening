import time


def test_correct_authorization(browser, main_page):
    # TODO инпутов логина и пароля нет на главной странице, они на странице /login
    #  А значит для проверки авторизации нужно создать новый PageObject LoginPage и работать с ним
    main_page.open()
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1234')
    # TODO Кнопку "Запомнить меня" можно пока убрать, она ничего не делает пока :)
    #  Тем более у тебя тест на базовую проверку работы авторизации,
    #  а запоминание не входит в базовую проверку
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL


def test_incorrect_password_authorization(browser, main_page):
    main_page.open()
    # TODO если видишь, что код повторяется из теста в тест,
    #  а меняются только входные данные - это верный признак того,
    #  что в PageObject нужно сделать метод.
    #  Примерная сигнатура метода: def login(self, username: str, password: str):
    main_page.login_input.send_keys('test@test.ru')
    main_page.password_input.send_keys('1235')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'login'


def test_incorrect_username_authorization(browser, main_page):
    main_page.open()
    main_page.login_input.send_keys('pykpyk@test.ru')
    main_page.password_input.send_keys('1234')
    main_page.check_remember_button.click()
    main_page.authorization_button.click()
    time.sleep(2)
    assert browser.current_url == main_page.URL + 'login'
