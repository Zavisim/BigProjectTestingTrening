from selenium.webdriver.common.by import By

from pages.base import BasePage


class IncomesPage(BasePage):
    URL = "http://147.45.145.230:5000/incomes"

    @property
    def add_income(self):
        return self.driver.find_element(By.ID, 'addRowBtn')

    def filter_category_income(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'select[name="category"]')

    @property
    def amount_income(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.centered [name="amount"]')

    @property
    def product_description_income(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="description"]')

    @property
    def save_button_income(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.save-btn')