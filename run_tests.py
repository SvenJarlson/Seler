import unittest
from tests.login_test import LoginTest

# Download tests, that you want to run
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# List of tests to run
tests_for_run = [
    login_test,
    # kolejny test
    # ...
]



# Create Test Suite by combining tests
test_suite = unittest.TestSuite(tests_for_run)

# Run tests
unittest.TextTestRunner().run(test_suite)