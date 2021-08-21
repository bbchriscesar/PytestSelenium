import pytest
from pageObjects.login import LoginElements
from utilities.BaseClass import BaseClass


@pytest.mark.login
class LoginTests(BaseClass):

    def test_Login(self):

        loginData = self.readJSONConfig('login')
        log = self.getLogger()

        # Input username
        self.sendKeys(LoginElements.inputUsername, loginData['username'])
        log.info('Input username')

        # Input password
        self.sendKeys(LoginElements.inputPassword, loginData['password'])
        log.info('Input password')

        # Click Submit button
        self.click(LoginElements.btnSubmit)
        log.info('Click Submit button')

        # Check page title
        assert self.verifyPageTitle() == loginData['loginPageTitle']
        log.info('Check page title')
