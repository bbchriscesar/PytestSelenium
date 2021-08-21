import inspect
import json
import logging
import sys
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def readJSONConfig(jsondata):
        with open('.\\data\\' + jsondata + '.json') as json_data:
            data = json.load(json_data)
        return data

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(loggerName + '.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyElementVisibility(self, locator):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.visibility_of_element_located((locator[0], locator[1])))
            return element
        except Exception as e:
            print(e)
            raise ValueError('Element not visible')

    def click(self, locator):
        wait = WebDriverWait(self.driver, 5)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.click()
        except Exception as e:
            print(e)
            raise ValueError('Element not found')

    def sendKeys(self, locator, data):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.clear()
            element.send_keys(data)
        except Exception as e:
            print(e)
            raise ValueError('Element not found')

    def verifyPageTitle(self):
        current = self.driver.title
        return current
