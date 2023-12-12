# 1. Import the files
import unittest
from tests.test_ContactFormTest import ContactFormTest
from tests.test_LocatorsTest import LocatorsTest

# 2. Create the object of the class using unitTest
contactFormTestCase = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
locatorTestCase = unittest.TestLoader().loadTestsFromTestCase(LocatorsTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([contactFormTestCase, locatorTestCase])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note: all the methods in test files should define in proper run order