from tests.basetest import BaseTest
from time import sleep


class CartTest(BaseTest):
    """
    Cart Test
    """

    def test_product_is_added_to_cart(self):
        """
        TC 001 : Product is added to the cart
        """
        home_page = self.homepage.get_rid_of_popups()
        watches_page = self.watchespage
        # enter the watches tab
        watches_page.select_watches_section()
        # sort by price
        watches_page.sort_by_price()
        # select a watch
        watches_page.select_a_watch()
        # add it to the cart
        watches_page.add_first_watch_to_the_cart()
        # open the cart
        watches_page.open_cart()
        # check if product was added to cart
        self.assertTrue(watches_page.product_list_in_cart)
        sleep(3)
