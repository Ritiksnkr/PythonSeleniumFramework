from utilities.Locators import SignIn_Locators
from selenium.webdriver.common.by import By


class SignIn:
    def __init__(self, driver):
        self.driver = driver
        self.clickSignin = SignIn_Locators.SignIn
        self.Submit = SignIn_Locators.Submit

        # Valid Credential
        self.UserEmail = SignIn_Locators.Email
        self.Pswrd = SignIn_Locators.Password

        # InValid Credential
        self.UserEmail2 = SignIn_Locators.Email
        self.Pswrd2 = SignIn_Locators.Password

    def ClickSignInBtn(self):
        self.driver.find_element(By.XPATH, self.clickSignin).click()

    # Methods for valid credential
    def EnterEmail(self, uemail):
        self.driver.find_element(By.ID, self.UserEmail).send_keys(uemail)

    def EnterPassword(self, password):
        self.driver.find_element(By.ID, self.Pswrd).send_keys(password)

    # Methods for Invalid credential
    def EnterEmail2(self, uemail2):
        self.driver.find_element(By.ID, self.UserEmail2).send_keys(uemail2)

    def EnterPassword2(self, password2):
        self.driver.find_element(By.ID, self.Pswrd2).send_keys(password2)

    def click_Submit(self):
        self.driver.find_element(By.ID, self.Submit).click()
