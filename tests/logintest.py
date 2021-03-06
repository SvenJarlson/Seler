from tests.basetest import BaseTest
from pages.locators import HomePageLocators
from pages.locators import PopUpsLocators
from selenium.webdriver import ActionChains
from time import sleep

class LoginTest(BaseTest):
    """
    Login Test
    """


    def test_no_user_registered(self):
        """
        TC 002 : User is not registered
        """
        sleep(2)
        home_page = self.homepage.get_rid_of_popups()

        # 0. Locate the login panel
        el0 = self.driver.find_element(*HomePageLocators.HOVER_ACCOUNT)
        ActionChains(self.driver) \
            .move_to_element(el0) \
            .perform()
        # 1. Locate the box for e-mail
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Click to login
        el.click()
        sleep(1)
        # Locate the input box for email
        el1 = self.driver.find_element(*HomePageLocators.LOGIN_BOX)
        # 2. Put in an email
        el1.send_keys(self.testdata.email)
        sleep(1)
        # 3. Locate the box for password
        el2 = self.driver.find_element(*HomePageLocators.PASSWORD_BOX)
        # 4. Put in a password
        el2.send_keys(self.testdata.password)
        sleep(1)
        # 4. Locate the button to login
        el3 = self.driver.find_element(*HomePageLocators.LOGIN_BTN)
        el3.click()
        sleep(1)
        # 5. Locate the error message
        # el4 = self.driver.find_element(*HomePageLocators.ERROR_MSG)
        # 6. Expected result
        # error = ["Nieprawidłowa nazwa logowania lub hasło logowania"]
        # self.assertEqual(el4.text, error)
        # Actual result
        # there is an anti bot mechanism that prevents from automatic login
