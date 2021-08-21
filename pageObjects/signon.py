from selenium.webdriver.common.by import By


class SignOnElements:

    def __init__(self, driver):
        self.driver = driver

    lnkSignOn = (By.XPATH, "//a[text()='SIGN-ON']")
    inputUserName = (By.NAME, "userName")
    inputPassword = (By.NAME, "password")
    btnSubmit = (By.NAME, "submit")