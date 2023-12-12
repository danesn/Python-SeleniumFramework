from selenium import webdriver
import utilities.CustomLogger as CL

class WebDriverClass:
    log = CL.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome("D:\Learn Automation Selenium\driver\chromedriver64\chromedriver.exe")
            self.log.info("Chrome Driver is initializing...")
        else:
            print("Browser Driver not Found")
            self.log.error("Browser Driver "+ browserName +" not Found")

        return driver
