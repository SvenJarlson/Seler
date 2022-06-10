from pages.homepage import HomePage
from tests.testdata import TestData
from pages.watchespage import ProductsPage
from pages.privacysettingspage import PrivacySettingsPage

from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://pl.aliexpress.com/")
        self.driver.implicitly_wait(10)
        # Create a class HomePage
        # To gain access to the page's mechanisms
        self.homepage = HomePage(self.driver)
        self.watchespage = ProductsPage(self.driver)
        self.privacysettingspage = PrivacySettingsPage(self.driver)
        self.testdata = TestData()

    def tearDown(self):
        self.driver.quit()