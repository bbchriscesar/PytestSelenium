from selenium.webdriver.common.by import By


class LoginElements:

    def __init__(self, driver):
        self.driver = driver

    inputUsername = (By.NAME, "userName")
    inputPassword = (By.NAME, "password")
    btnSubmit = (By.NAME, "submit")

