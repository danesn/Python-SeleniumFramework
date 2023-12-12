from traceback import print_stack

from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utilities.CustomLogger as CL
import allure

class BaseClass:
    log = CL.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.warning("Something wrong!")
            self.log.info("Page title : " + self.driver.title)
            self.log.info("Web Page not Launched with URL : " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type " + locatorType + " is not Found!")
        return False

    def getWebElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info("WebElement Found with locator value " + locatorValue + " using locator type " + locatorByType)
        except:
            self.log.error("WebElement not Found with locator value " + locatorValue + " using locator type " + locatorByType)
            print_stack()
            assert False
        return webElement

    def waitForElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)

            wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=None)
            webElement = wait.until(EC.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElement Found with locator value " + locatorValue + " using locator type " + locatorByType)
        except:
            self.log.error("WebElement not Found with locator value " + locatorValue + " using locator type " + locatorByType)
            print_stack()
            # Save Screenshot
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            # locatorByType = self.getLocatorType(locatorType)

            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info("Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to Send the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            # Save Screenshot
            self.takeScreenshot(locatorType)
            assert False

    def getText(self, locatorValue, locatorType="id"):
        webElement = None
        elementText = None
        try:
            locatorType = locatorType.lower()
            # locatorByType = self.getLocatorType(locatorType)
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info("Got the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to get the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            assert False

        return elementText

    def isElementDisplayed(self, locatorValue, locatorType="id"):
        webElement = None
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info("WebElement is Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("WebElement is not Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            assert False

        return elementDisplayed

    def scrollTo(self, locatorValue, locatorType):
        webElement = None
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info("Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error("Unable to scroll to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            assert False

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)