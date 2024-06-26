from selenium.webdriver.common.by import By

from elements.element import Element
from pages.base import BasePage


class StatisticsPage(BasePage):
    URL = "http://147.45.145.230:5000/statistics"

    @property
    def table_1_plan(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-category-id="1"] .plan-for-category')

    @property
    def table_1_plan_input(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-category-id="1"] .plan-for-category input')

    @property
    def statistics(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.navbar a[href="/statistics"]')
