from base.DriverClass import WebDriverClass
from base.BaseClass import BaseClass
from pages.ContactFormPage import ContactForm

import time

# Script
# 1. Create WebDriver Class object and get Return Driver Variable
wd = WebDriverClass()
driver = wd.getWebDriver("chrome")
driver.maximize_window()

# 2. Create BasePage Class object
bp = BaseClass(driver=driver)
cf = ContactForm(driver=driver)
bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")

cf.clickContactForm()
time.sleep(3)
cf.verifyFormContainer()

cf.enterName()
cf.enterEmail()

cf.clickRadioGender()

cf.enterTechnology()
cf.enterMessage()
cf.getCaptcha()
cf.enterCaptcha()
time.sleep(3)

cf.clickOnPostButton()
time.sleep(5)

# Test 1
# element = bp.getWebElement("user_input", "id")
# element = bp.waitForElement("user_input", "id")
# print(element.get_attribute("class"))
# element.send_keys("Tester")

# Test 2
# bp.sendText("Yuhuy", "user_input", "id")
# tata = bp.getWebElement("h1", "tag")
# tata = bp.getText("//input[contains(@value, 'Button2')]", "xpath")
# bp.clickOnElement("Form", "link")
# print("aaaa", tata.text)

# Test 3
# ele = bp.isElementDisplayed("user_input", "id")
# print(ele)
# bp.sendText("yayaya", "user_input" , "id")

# Test 4
# bp.scrollTo("footer-left", "class")
# time.sleep(3)

driver.quit()