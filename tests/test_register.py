import pytest
from pageObjects.register import RegisterElements
from utilities.BaseClass import BaseClass


@pytest.mark.register
class RegisterTests(BaseClass):

    def test_register(self):

        loginData = self.readJSONConfig('register')
        log = self.getLogger()

        # Click Register
        self.click(RegisterElements.lnkRegister)
        log.info('Click Register')

        # Input first name
        self.sendKeys(RegisterElements.inputFirstName, loginData['FirstName'])
        log.info('Input first name')

        # Input last name
        self.sendKeys(RegisterElements.inputLastName, loginData['LastName'])
        log.info('Input last name')

        # Input phone
        self.sendKeys(RegisterElements.inputPhone, loginData['Phone'])
        log.info('Input phone')

        # Input email
        self.sendKeys(RegisterElements.inputEmail, loginData['Email'])
        log.info('Input email')

        # Input address
        self.sendKeys(RegisterElements.inputAddress, loginData['Address'])
        log.info('Input address')

        # Input city
        self.sendKeys(RegisterElements.inputCity, loginData['City'])
        log.info('Input city')

        # Input state
        self.sendKeys(RegisterElements.inputState, loginData['State'])
        log.info('Input state')

        # Input postal code
        self.sendKeys(RegisterElements.inputPostalCode, loginData['PostalCode'])
        log.info('Input postal code')

        # Input user name
        self.sendKeys(RegisterElements.inputUserName, loginData['Username'])
        log.info('Input user name')

        # Input password
        self.sendKeys(RegisterElements.inputPassword, loginData['Password'])
        log.info('Input password')

        # Input confirm password
        self.sendKeys(RegisterElements.inputConfirmPassword, loginData['ConfirmPassword'])
        log.info('Input confirm password')

        # Click submit button
        self.click(RegisterElements.btnSubmit)
        log.info('Click submit button')
