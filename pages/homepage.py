from pages.basepage import BasePage
from pages.locators import PopUpsLocators
from pages.locators import SearchPageLocators
from time import sleep


class HomePage(BasePage):
    """
    Landing Page Object
    """
    def get_rid_of_popups(self):
        """
        Clicks close on the popups
        """
        sleep(4)
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
        # return this page
        return HomePage(self.driver)

    def _verify_page(self):
        """
        Verifies Home Page
        """
        pass

    def input_for_search_product(self):
        # locate the search input
        inp = self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)
        # put in the product name
        inp.send_keys("zegarek")

    def search_product(self):
        # locate the search button
        btn = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        # click the button
        btn.click()

    def locate_results(self):
        # locate the results
        results = self.driver.find_elements(*SearchPageLocators.SEARCH_RESULTS)
        for i in range(len(results)):
            results[i] = results[i].get_attribute('textContent')
        return results
