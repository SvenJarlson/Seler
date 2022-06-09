from pages.basepage import BasePage
from pages.locators import PopUpsLocators


class HomePage(BasePage):
    """
    Landing Page Object
    """
    def get_rid_of_popups(self):
        """
        Clicks close on the popups
        """
        # 1. conditionally locate first pop-up and click it
        if self.driver.find_element(*PopUpsLocators.COOKIES_BTN):
            el = self.driver.find_element(*PopUpsLocators.COOKIES_BTN)
            el.click()
        else:
            pass
        # 2. conditionally locate second pop-up and click it
        if self.driver.find_element(*PopUpsLocators.COOKIES_BTN2):
            el1 = self.driver.find_element(*PopUpsLocators.COOKIES_BTN2)
            el1.click()
        else:
            pass
        # 3. Conditionally locate third pop-up and click it
        if self.driver.find_element(*PopUpsLocators.DISCOUNT_AD_BTN):
            el2 = self.driver.find_element(*PopUpsLocators.DISCOUNT_AD_BTN)
            el2.click()
        else:
            pass

    def _verify_page(self):
        """
        Verifies Home Page
        """
        pass
