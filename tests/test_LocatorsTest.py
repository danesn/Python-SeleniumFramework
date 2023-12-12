import unittest
import pytest

from base.BaseClass import BaseClass
from pages.LocatorsPage import Locators


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LocatorsTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.bp = BaseClass(self.driver)
        self.lp = Locators(self.driver)

    @pytest.mark.run(order=3)
    def test_locatorPage(self):
        self.lp.clickLocatorsPage()

    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=5)
    def test_enterDataInLocatorForm(self):
        self.lp.enterTextInput()
        self.lp.clickOnSubmitButton()
        self.lp.verifyValue()
