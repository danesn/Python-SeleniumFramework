import time
import pytest
from base.BaseClass import BaseClass
from base.DriverClass import WebDriverClass

@pytest.fixture(scope="class")
def beforeClass(request):

    # __Before Class__
    print("Before Class")
    # Create WebDriverClass object and BaseClass object
    web_driver = WebDriverClass()
    driver = web_driver.getWebDriver('chrome')
    base_page = BaseClass(driver)
    # Launch web page with URL
    base_page.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
    if request.cls is not None:
        request.cls.driver = driver

    # __After Class__
    yield driver # Return Yield object
    time.sleep(5)
    driver.quit()
    print("After Class")

@pytest.fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")