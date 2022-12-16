import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.Locators import Address_Locators


class Add_New_Address:
    def __init__(self, driver):
        self.driver = driver

        self.SignIn = Address_Locators.SignIn
        self.u_email = Address_Locators.Email
        self.Password = Address_Locators.Password
        self.Submit_Btn = Address_Locators.Submit

        self.Add_AddressBtn = Address_Locators.AddressBtn
        self.Add_New_AddressBtn = Address_Locators.Add_New_Address
        self.FirstName = Address_Locators.FirstName
        self.LastName = Address_Locators.LastName
        self.Company = Address_Locators.Company
        self.Address1 = Address_Locators.addrs
        self.Address2 = Address_Locators.addrs2
        self.City = Address_Locators.city
        self.State = Address_Locators.state
        self.zipcode = Address_Locators.pcode
        self.Country = Address_Locators.cntry
        self.Hphone = Address_Locators.home
        self.Mphone = Address_Locators.phone
        self.AddInfo = Address_Locators.Other
        self.Addrs_Title = Address_Locators.address_title
        self.Save = Address_Locators.SaveButton

    def click_SignIn(self):
        self.driver.find_element(By.XPATH, self.SignIn).click()

    def login(self, UEMAIL, PSWRD):
        self.driver.find_element(By.ID, self.u_email).send_keys(UEMAIL)
        self.driver.find_element(By.ID, self.Password).send_keys(PSWRD)
        self.driver.find_element(By.ID, self.Submit_Btn).click()

    def goto_add_new_address(self):
        self.driver.find_element(By.XPATH, self.Add_AddressBtn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Add_New_AddressBtn).click()

    def enter_new_address_details(self, fname, lname, cname, a1, a2, city, state, zipcode, country, phoneH, phoneM,
                                  Info, Title):
        FIRST_NAME = self.driver.find_element(By.XPATH, self.FirstName)
        FIRST_NAME.clear()
        FIRST_NAME.send_keys(fname)

        LAST_NAME = self.driver.find_element(By.XPATH, self.LastName)
        LAST_NAME.clear()
        LAST_NAME.send_keys(lname)

        COMPANY = self.driver.find_element(By.ID, self.Company)
        COMPANY.clear()
        COMPANY.send_keys(cname)

        self.driver.find_element(By.ID, self.Address1).send_keys(a1)
        self.driver.find_element(By.ID, self.Address2).send_keys(a2)
        self.driver.find_element(By.ID, self.City).send_keys(city)
        State = Select(self.driver.find_element(By.NAME, self.State))
        State.select_by_value(state)
        self.driver.find_element(By.XPATH, self.zipcode).send_keys(zipcode)
        cntry = Select(self.driver.find_element(By.NAME, self.Country))
        cntry.select_by_value(country)

        self.driver.find_element(By.ID, self.Hphone).send_keys(phoneH)
        self.driver.find_element(By.ID, self.Mphone).send_keys(phoneM)
        self.driver.find_element(By.ID, self.AddInfo).send_keys(Info)
        TITLE = self.driver.find_element(By.ID, self.Addrs_Title)
        TITLE.clear()
        TITLE.send_keys(Title)
        self.driver.find_element(By.ID, self.Save).click()
