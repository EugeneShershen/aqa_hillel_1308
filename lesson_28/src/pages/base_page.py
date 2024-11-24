from selenium.webdriver.remote.webdriver import WebDriver

from lesson_28.src.pages.element_actions import ElementActions


class BasePage:
    """Base class for pages."""
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ElementActions(driver)
        self.base_url = "https://guest:welcome2qauto@qauto2.forstudy.space"
