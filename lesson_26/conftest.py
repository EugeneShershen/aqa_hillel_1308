import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8000/lesson_26/src/dz.html")

    yield driver

    driver.quit()
