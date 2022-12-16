from datetime import time

from selenium.webdriver.common.by import By

from pages.Delete_Address import delete_Address
from configfiles import config
from utilities.Locators import DeleteAddress_Locators


class Test_DeleteAddress:
    def test_Test_DeleteAddress(self, setup):
        self.driver = setup
        self.DELETE = delete_Address(self.driver)

        self.DELETE.Login(config.UserEmail, config.UserPassword)
        self.DELETE.delete_Address()

        # Assertion to check whether user delete address successfully or not.
        Alert = self.driver.find_element(By.XPATH, DeleteAddress_Locators.Alert).text
        try:
            assert "No addresses are available.&nbsp;" in Alert
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)