import os
from datetime import datetime
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=".\\drivers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=".\\drivers\\geckodriver.exe")
    driver.maximize_window()
    driver.get("http://demo.guru99.com/test/newtours/")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Regression Travel Tours"


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")