from tests.basetest import BaseTest
from time import sleep
from pages.locators import HomePageLocators
import unittest

class LoginTest(BaseTest):
    """
    Login Test
    """


    def test_no_user_registered(self):
        """
        TC 002 : User is not registered
        """
        home_page = self.home_page
        # 0. Locate the login panel
        el1 = self.driver.find_element(*HomePageLocators.HOVER_ACCOUNT)
        el1.click()
        # 1. Locate the box for e-mail
        el = self.driver.find_element(*HomePageLocators.LOGIN_BOX) 
        # 2. Pun in an email
        el.send_keys(self.test_data.email)
        # 3. Locate the box for password
        el2 = self.driver.find_element(*HomePageLocators.PASSWORD_BOX)
        # 4. Put in a password
        el2.send_keys(self.test_data.password)
        # 4. Locate the button to login
        el3 = self.driver.find_element(*HomePageLocators.LOGIN_BTN)
        el3.click()
        # 5. Locate the error message
        el4 = self.driver.find_element(*HomePageLocators.ERROR_MSG)        
        # 6. Expected result
        error = ["Nieprawidłowa nazwa logowania lub hasło logowania"]
        self.assertEqual(el4.text, error)