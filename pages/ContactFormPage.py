from base.BaseClass import BaseClass
import utilities.CustomLogger as CL

class ContactForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values in Contact Form page
    _contactFormPage = "Form" # link
    _formContainer = "reused_form" # id
    _inputName = "name" # id
    _inputEmail = "email" # id
    _radioGender = "//input[contains(@value, 'female')]" # xpath
    _inputTechno = "tech" # id
    _textareaMessage = "//textarea[contains(@name, 'message')]" # xpath
    _textCaptchaImage = "captcha_image" # id
    _inputCaptchaImage = "captcha" # name
    _btnPost = "btnContactUs" # id

    def clickContactForm(self):
        self.clickOnElement(self._contactFormPage, 'link')
        CL.allureLogs("Clicked on Contact Form")

    def verifyFormContainer(self):
        element = self.isElementDisplayed(self._formContainer, 'id')
        assert element == True
        CL.allureLogs("Verified Contact Form")

    def enterName(self):
        self.sendText("Yoman man", self._inputName, 'id')
        CL.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("Yoman@mail.com", self._inputEmail, 'id')
        CL.allureLogs("Entered Email")

    def clickRadioGender(self, gender="female"):
        self.clickOnElement(self._radioGender, 'xpath')
        CL.allureLogs("Clicked on Radio Gender:Female")

    def enterTechnology(self):
        self.sendText("new automation learning from udemy", self._inputTechno, 'id')
        CL.allureLogs("Entered Technology")

    def enterMessage(self):
        self.sendText("this is the new message", self._textareaMessage, 'xpath')
        CL.allureLogs("Entered Message")

    def getCaptcha(self):
        textCaptcha = self.getText(self._textCaptchaImage, 'id')
        CL.allureLogs("Got the captcha data")
        return textCaptcha

    def enterCaptcha(self):
        self.scrollTo(self._inputCaptchaImage, 'name')
        self.sendText(self.getCaptcha(), self._inputCaptchaImage, 'name')
        CL.allureLogs("Entered Captcha")

    def clickOnPostButton(self):
        self.scrollTo(self._btnPost, 'id')
        self.clickOnElement(self._btnPost, 'id')
        CL.allureLogs("Clicked on the post button")
