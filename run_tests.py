import unittest
from tests.logintest import LoginTest
from tests.carttest import CartTest

# Download tests, that you want to run
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
cart_test = unittest.TestLoader().loadTestsFromTestCase(CartTest)
# List of tests to run
tests_for_run = [
    #login_test,
    cart_test
    # next test
]

# Create Test Suite by combining tests
test_suite = unittest.TestSuite(tests_for_run)

# Run tests
unittest.TextTestRunner().run(test_suite)
