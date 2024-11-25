import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from faker import Faker


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def fake_user():
    faker = Faker()

    fake_user = (faker.first_name(), faker.last_name(), faker.email(), faker.password(
        length=10, digits=True, upper_case=True, lower_case=True))

    yield fake_user
