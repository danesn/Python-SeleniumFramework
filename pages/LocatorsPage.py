from base.BaseClass import BaseClass
import utilities.CustomLogger as CL


class Locators(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values in Enter Text Page
    _enterTextPage = "Locators" # link
    _inputText = "user_input" # id
    _btnSubmit = "submitbutton" # id
    _displayValue = "display" # id

    def clickLocatorsPage(self):
        self.clickOnElement(self._enterTextPage, 'link')
        CL.allureLogs("Clicked on Locators Page")

    def enterTextInput(self):
        textElement = "Yono Zono 123"
        self.sendText(textElement, self._inputText, 'id')
        CL.allureLogs("Entered Text to Input Text")

    def clickOnSubmitButton(self):
        self.scrollTo(self._displayValue, 'id')
        self.clickOnElement(self._btnSubmit, 'id')
        CL.allureLogs("Clicked on Submit Button")

    def verifyValue(self):
        textElementResult = self.getText(self._displayValue, 'id')
        assert textElementResult == "Yono Zono 123"
        CL.allureLogs("Verify textResult Value")
