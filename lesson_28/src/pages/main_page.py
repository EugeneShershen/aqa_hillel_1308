from selenium.webdriver.common.by import By

from lesson_28.src.pages.base_page import BasePage
from lesson_28.src.pages.main_page_elements.sign_in import SignIn
from lesson_28.src.pages.main_page_elements.sign_up import SignUp


class MainPage(BasePage):
    """Class for the main page."""
    __SIGN_IN_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-white.header_signin")
    __SIGN_UP_BTN = (By.CSS_SELECTOR, ".hero-descriptor_btn.btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in = SignIn(driver)
        self.sign_up = SignUp(driver)

    def open(self):
        self.driver.get(self.base_url)

    def click_sign_in_btn(self):
        self.actions.click(self.__SIGN_IN_BTN)

    def click_sign_up_btn(self):
        self.actions.click(self.__SIGN_UP_BTN)
