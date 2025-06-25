import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'Firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        raise ValueError('unsupported browser')
    return driver


