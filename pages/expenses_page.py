from selenium.webdriver.common.by import By

from pages.base import BasePage


class ExpensesPage(BasePage):
    URL = "http://147.45.145.230:5000/expenses"

    @property
    def add_value(self):
        return self.driver.find_element(By.ID, 'addRowBtn')

    @property
    def filter_category_expenses(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'select[name="category"]')

    @property
    def filter_month_expenses(self):
        return self.driver.find_element(By.ID, 'monthFilter')

    @property
    def amount_expenses(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.centered [name="amount"]')

    @property
    def product_description_expenses(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="description"]')

    @property
    def save_button_expenses(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.save-btn')

    @property
    def delete_product_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.btn-delete[data-id="19"]')

    @property
    def description(self):
        return self.driver.find_element(By.CLASS_NAME, 'description')
