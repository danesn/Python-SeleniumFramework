import time
import unittest
import pytest

from base.BaseClass import BaseClass
from pages.ContactFormPage import ContactForm


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    # Setelah BeforeClass dan BeforeMethod fixture, maka classObject fixture dijalankan
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.clickContactForm()
        self.cf.verifyFormContainer()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.clickRadioGender()
        self.cf.enterTechnology()
        self.cf.enterMessage()
        self.cf.enterCaptcha()
        self.cf.clickOnPostButton()

