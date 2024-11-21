import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()
