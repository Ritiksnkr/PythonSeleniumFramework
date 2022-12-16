from selenium.webdriver.common.by import By
from utilities.Locators import SearchPage_Locators


class Item_Search:
    def __init__(self, driver):
        self.driver = driver

        self.SignIn = SearchPage_Locators.SignIn
        self.Email = SearchPage_Locators.Email
        self.Pswrd = SearchPage_Locators.Password
        self.Submit = SearchPage_Locators.Submit
        self.EnterItem = SearchPage_Locators.SearchBox
        self.SearchItem = SearchPage_Locators.SearchBtn

    def login(self, UEMAIL, PSWRD):
        self.driver.find_element(By.XPATH, self.SignIn).click()
        self.driver.find_element(By.ID, self.Email).send_keys(UEMAIL)
        self.driver.find_element(By.ID, self.Pswrd).send_keys(PSWRD)
        self.driver.find_element(By.ID, self.Submit).click()

    def searchItem(self, Item):
        self.driver.find_element(By.ID, self.EnterItem).send_keys(Item)
        self.driver.find_element(By.XPATH, self.SearchItem).click()
