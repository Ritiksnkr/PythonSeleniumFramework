from selenium.webdriver.common.by import By

from utilities.Locators import DeleteAddress_Locators


class delete_Address:
    def __init__(self, driver):
        self.driver = driver
        self.SignInBtn = DeleteAddress_Locators.SignIn
        self.User_Email = DeleteAddress_Locators.Email
        self.User_Pswrd = DeleteAddress_Locators.Password
        self.Submit = DeleteAddress_Locators.Submit
        self.AddressBtn = DeleteAddress_Locators.AddressBtn
        self.Delete_Address = DeleteAddress_Locators.Delete_Btn

    def Login(self, UEMAIL, PSWRD):
        self.driver.find_element(By.XPATH, self.SignInBtn).click()
        self.driver.find_element(By.ID, self.User_Email).send_keys(UEMAIL)
        self.driver.find_element(By.ID, self.User_Pswrd).send_keys(PSWRD)
        self.driver.find_element(By.ID, self.Submit).click()

    def delete_Address(self):
        self.driver.find_element(By.XPATH, self.AddressBtn).click()
        self.driver.find_element(By.XPATH, self.Delete_Address).click()
        self.driver.switch_to.alert.accept()
