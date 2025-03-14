import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser..........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser..........")
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")   # send browser value to setup method


##############  PyTest HTML Report  ##################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nop Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Lei"

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)








