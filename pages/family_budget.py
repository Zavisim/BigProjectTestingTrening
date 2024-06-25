import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base import BasePage


class FamilyBudget(BasePage):
    URL = "http://147.45.145.230:5000"


