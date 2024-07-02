from selenium.webdriver.common.by import By

from pages.base import BasePage

from elements.element import Element


class MainPage(BasePage):
    URL = "http://147.45.145.230:5000/"

    # TODO блок кода ниже вынести в PageObject LoginPage
    @property
    def login_input(self):
        return self.driver.find_element(By.ID, 'email')

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, 'password')

    @property
    def check_remember_button(self):
        return self.driver.find_element(By.ID, 'remember')

    @property
    def authorization_button(self):
        return self.driver.find_element(By.ID, 'submit')

    # TODO блок кода выше вынести в PageObject LoginPage

    @property
    def diagrams(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/"]')

    @property
    def statistics(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/statistics"]')

    @property
    def expenses(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/expenses"]')

    @property
    def incomes(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/incomes"]')

    @property
    def imports(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/bank-import"]')

    @property
    def logout(self):
        return Element(self.driver, By.CSS_SELECTOR, '.profile a[href="/logout"]')

    @property
    def logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.logo a[href="/"]')
