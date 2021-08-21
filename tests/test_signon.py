import pytest
from pageObjects.signon import SignOnElements
from utilities.BaseClass import BaseClass


@pytest.mark.signon
class SignOnTests(BaseClass):

    def test_signon(self):

        loginData = self.readJSONConfig('signon')
        log = self.getLogger()

        # Click sign on
        self.click(SignOnElements.lnkSignOn)
        log.info('Click submit sign on')

        # Input username
        self.sendKeys(SignOnElements.inputUserName, loginData['username'])
        log.info('Input username')

        # Input password
        self.sendKeys(SignOnElements.inputPassword, loginData['password'])
        log.info('Input password')

        # Click submit button
        self.click(SignOnElements.btnSubmit)
        log.info('Click submit button')
