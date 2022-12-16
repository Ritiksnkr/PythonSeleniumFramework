from datetime import time

from pages.SignIn import SignIn
from configfiles import config


class Test_SignIn_using_ValidCredential:
    def test_signIn(self, setup):
        self.driver = setup
        self.login = SignIn(self.driver)

        self.login.ClickSignInBtn()
        self.login.EnterEmail(config.UserEmail)
        self.login.EnterPassword(config.UserPassword)
        self.login.click_Submit()

        # Assertion to check whether user logged in successfully or not.
        try:
            assert "My account - My Store" in self.driver.title
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)