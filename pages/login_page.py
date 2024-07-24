import time

from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    URL = "http://147.45.145.230:5000/login"

    @property
    def login_input(self):
        return self.driver.find_element(By.ID, 'login')

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, 'password')

    @property
    def check_remember_button(self):
        return self.driver.find_element(By.ID, 'remember')

    @property
    def authorization_button(self):
        return self.driver.find_element(By.ID, 'submit')

    def login(self, username: str, password: str):
        self.open()
        self.login_input.send_keys(username)
        self.password_input.send_keys(password)
        self.authorization_button.click()
        time.sleep(2)
