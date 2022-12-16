import time

from selenium.webdriver.common.by import By

from configfiles import config
from pages.Add_Address import Add_New_Address
from utilities.Locators import Address_Locators


class Test_AddAddress:
    def test_AddAddress(self, setup):
        self.driver = setup
        self.new_addrs = Add_New_Address(self.driver)

        self.new_addrs.click_SignIn()
        self.new_addrs.login(config.UserEmail, config.UserPassword)

        self.new_addrs.goto_add_new_address()
        self.new_addrs.enter_new_address_details(config.New_Fname, config.New_Lname, config.New_Company,
                                                 config.New_Address1, config.New_Address2, config.New_City,
                                                 config.New_State, config.zipcode, config.New_Country,
                                                 config.New_hphone, config.New_mphone, config.Add_Info,
                                                 config.Address_Title)

        # Assertion to check whether User Added address successfully or not
        Subheading = self.driver.find_element(By.XPATH, Address_Locators.Subheading).text
        try:
            assert config.Address_Title in Subheading
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)