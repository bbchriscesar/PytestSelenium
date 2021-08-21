import json

from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Code\\PytestSelenium\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://demo.guru99.com/test/newtours/")
    request.cls.driver = driver
    yield
    driver.quit()


