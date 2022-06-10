from pages.basepage import BasePage
from pages.locators import SelectWatchesLocators
from time import sleep

class ProductsPage(BasePage):

    def select_watches_section(self):
        # locate the link
        el = self.driver.find_element(*SelectWatchesLocators.WATCHES_BTN)
        # click on it
        el.click()

    def sort_by_price(self):
        # locate the button
        el1 = self.driver.find_element(*SelectWatchesLocators.PRICE_SORT)
        # click on it
        el1.click()
        sleep(2)

    def select_a_watch(self):
        # locate a watch
        el2 = self.driver.find_elements(*SelectWatchesLocators.SELECT_WATCH)[1]
        # click on it
        el2.click()

    def add_first_watch_to_the_cart(self):
        # locate button
        el3 = self.driver.find_element(*SelectWatchesLocators.ADD_TO_CART)
        # click on it
        el3.click()

    def open_cart(self):
        # locate the button
        el4 = self.driver.find_element(*SelectWatchesLocators.SHOW_CART)
        # click on it
        el4.click()
        sleep(1)

    def product_list_in_cart(self):
        # locate the button
        el5 = self.driver.find_element(*SelectWatchesLocators.FIND_IN_CART)

