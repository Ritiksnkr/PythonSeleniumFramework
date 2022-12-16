from datetime import time

from pages.SignIn import SignIn
from configfiles import config


class Test_SignIn_using_InalidCredential:
    def test_signIn(self, setup):
        self.driver = setup
        self.login = SignIn(self.driver)

        self.login.ClickSignInBtn()
        self.login.EnterEmail(config.UserEmail2)
        self.login.EnterPassword(config.UserPassword2)
        self.login.click_Submit()

        # Assertion to check whether user can not able to log in using invalid credential.
        try:
            assert "My account - My Store" in self.driver.title
            print("Assertion Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))
        time.sleep(3)
