import pytest
from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from configfiles import config


@pytest.fixture()
def setup():
    global driver
    if config.node.lower() == "non-headless":
        if config.browser.lower() == "chrome":
            driver = webdriver.Chrome(config.ChromeDriverLocation)
        elif config.browser.lower() == "edge":
            driver = webdriver.Edge(config.EdgeDriverLocation)
        elif config.browser.lower() == "firefox":
            driver = webdriver.Firefox(config.FirefoxDriverLocation)
        else:
            print("Browser name is invalid")
    if config.node.lower() == "headless":
        if config.browser.lower() == "chrome":
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(config.ChromeDriverLocation, options=options)
        elif config.browser.lower() == "edge":
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(config.ChromeDriverLocation, options=options)
        elif config.browser.lower() == "firefox":
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(config.ChromeDriverLocation, options=options)
        else:
            print("Browser name is invalid")

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(config.baseUrl)

    yield driver
    driver.implicitly_wait(15)
    driver.close()
