from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.Locators import SignUp_Locators


class Sign_Up:
    def __init__(self, driver):
        self.driver = driver

        self.signin_btn = SignUp_Locators.SignInBtn
        self.email = SignUp_Locators.EnterEmail
        self.createAccount = SignUp_Locators.CreateAccount
        self.prefix = SignUp_Locators.Prefix
        self.fname = SignUp_Locators.FirstName
        self.lname = SignUp_Locators.LastName
        self.pswrd = SignUp_Locators.Password
        self.day = SignUp_Locators.Days
        self.month = SignUp_Locators.month
        self.year = SignUp_Locators.year
        self.Comp = SignUp_Locators.Company
        self.address = SignUp_Locators.addrs
        self.address2 = SignUp_Locators.addrs2
        self.city = SignUp_Locators.city
        self.State = SignUp_Locators.state
        self.zip = SignUp_Locators.pcode
        self.Country = SignUp_Locators.cntry
        self.adinfo = SignUp_Locators.Other
        self.homePhone = SignUp_Locators.home
        self.mobilePhone = SignUp_Locators.phone
        self.addAlias = SignUp_Locators.alias_for_future
        self.Register = SignUp_Locators.SubmitBtn

    def click_SignIn(self):
        self.driver.find_element(By.XPATH, self.signin_btn).click()

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.email).send_keys(email)

    def click_CreateAccount(self):
        self.driver.find_element(By.ID, self.createAccount).click()

    def Select_Prefix(self):
        self.driver.find_element(By.ID, self.prefix).click()

    def FirstName(self, fname):
        self.driver.find_element(By.XPATH, self.fname).send_keys(fname)

    def LstName(self, lname):
        self.driver.find_element(By.XPATH, self.lname).send_keys(lname)

    def Password(self, pswrd):
        self.driver.find_element(By.XPATH, self.pswrd).send_keys(pswrd)

    def DOB(self, Day, Month, Year):
        day = Select(self.driver.find_element(By.XPATH, self.day))
        day.select_by_value(Day)
        month = Select(self.driver.find_element(By.XPATH, self.month))
        month.select_by_value(Month)
        year = Select(self.driver.find_element(By.XPATH, self.year))
        year.select_by_value(Year)

    def Company(self, cname):
        self.driver.find_element(By.ID, self.Comp).send_keys(cname)

    def Address(self, a1, a2, city, state, zipcode, country):
        self.driver.find_element(By.ID, self.address).send_keys(a1)
        self.driver.find_element(By.ID, self.address2).send_keys(a2)
        self.driver.find_element(By.ID, self.city).send_keys(city)
        State = Select(self.driver.find_element(By.NAME, self.State))
        State.select_by_value(state)
        self.driver.find_element(By.XPATH, self.zip).send_keys(zipcode)
        cntry = Select(self.driver.find_element(By.NAME, self.Country))
        cntry.select_by_value(country)

    def Info(self, Info, homeMob, Mob, Alias):
        self.driver.find_element(By.ID, self.adinfo).send_keys(Info)
        self.driver.find_element(By.ID, self.homePhone).send_keys(homeMob)
        self.driver.find_element(By.ID, self.mobilePhone).send_keys(Mob)
        self.driver.find_element(By.ID, self.addAlias).send_keys(Alias)

    def Submit(self):
        self.driver.find_element(By.ID, self.Register).click()
