import time

import pytest

from selenium.webdriver.chrome import webdriver

def setup():
    print('set up')
    driver = webdriver.WebDriver(executable_path='chromedriver.exe')

    driver.get('https://habr.com/ru/all/')
    time.sleep(2)
    return driver

def tear_down(driver):
    print('tear down')
    driver.quit()

@pytest.fixture
def driver():
    obj = setup()

    yield obj

    tear_down(obj)