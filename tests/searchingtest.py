from tests.basetest import BaseTest
from time import sleep


class SearchingTest(BaseTest):
    """
    Search Test
    """

    def test_search_engine_result(self):
        """
        TC 004 : Searching a product by name
        """
        sleep(1)
        home_page = self.homepage.get_rid_of_popups()
        # locate the search bar and put in the product name
        home_page.input_for_search_product()
        # search the product
        home_page.search_product()
        # locate the results
        results = home_page.locate_results()
        # test if the results have product name at least once
        result = 0
        for word in results:
            if word.find("zegarek"):
                result = result +1
            else:
                pass
            return result
        self.assertGreater(result, 0)
