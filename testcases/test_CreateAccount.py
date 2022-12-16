import random
import time

from pages.CreateAccount import Sign_Up
from configfiles import config


class Test_signUp:
    def test_createAccount(self, setup):
        self.driver = setup
        self.ca = Sign_Up(self.driver)
        self.ca.click_SignIn()
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(2)
        randomEmail = random.choice(config.letters) + "867@gmail.com"
        self.ca.Enter_Email(randomEmail)
        self.ca.click_CreateAccount()
        self.driver.implicitly_wait(5)
        self.ca.Select_Prefix()
        self.ca.FirstName(config.First_Name)
        self.ca.LstName(config.Last_Name)
        self.ca.Password(config.Password)
        time.sleep(2)
        self.ca.DOB(config.Day, config.Month, config.Year)
        self.ca.Company(config.Company)
        self.ca.Address(config.Address, config.Address2, config.City, config.State, config.zipcode, config.Country)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        self.ca.Info(config.AddInfo, config.homePhone, config.phone, config.Alias)
        self.ca.Submit()
        self.driver.implicitly_wait(5)

        # Assertion to check whether user successfully able to create new account.
        try:
            assert "My account - My Store" in self.driver.title
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)

