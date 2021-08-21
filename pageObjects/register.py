from selenium.webdriver.common.by import By


class RegisterElements:

    def __init__(self, driver):
        self.driver = driver

    lnkRegister = (By.XPATH, "//a[text()='REGISTER']")
    inputFirstName = (By.NAME, "firstName")
    inputLastName = (By.NAME, "lastName")
    inputPhone = (By.NAME, "phone")
    inputEmail = (By.NAME, "userName")
    inputAddress = (By.NAME, "address1")
    inputCity = (By.NAME, "city")
    inputState = (By.NAME, "state")
    inputPostalCode = (By.NAME, "postalCode")
    inputUserName = (By.NAME, "email")
    inputPassword = (By.NAME, "password")
    inputConfirmPassword = (By.NAME, "confirmPassword")
    btnSubmit = (By.NAME, "submit")

