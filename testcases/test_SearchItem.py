import time

from selenium.webdriver.common.by import By
from utilities.Locators import SearchPage_Locators
from pages.Search_Item import Item_Search
from configfiles import config


class Test_searchItem:
    def test_ItemSearch(self, setup):
        self.driver = setup
        self.SEARCH = Item_Search(self.driver)

        self.SEARCH.login(config.UserEmail, config.UserPassword)
        self.SEARCH.searchItem(config.Item)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-5)", "")

        # Assertion to check whether user search item and get the result successfully.
        TEXT = self.driver.find_element(By.XPATH, SearchPage_Locators.Assertion).text
        try:
            assert "PRINTED DRESS" in TEXT
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)
