from selenium.webdriver.common.by import By

from pages.base import BasePage


class ExpensesPage(BasePage):
    URL = "http://147.45.145.230:5000/expenses"

    @property
    def add_value(self):
        return self.driver.find_element(By.ID, 'addRowBtn')

    @property
    def choice_category(self):
        return self.driver.find_element(By.ID, 'category')

    @property
    def filter_month(self):
        return self.driver.find_element(By.ID, 'monthFilter')