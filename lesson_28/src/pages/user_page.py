from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.src.pages.base_page import BasePage
from lesson_28.src.pages.user_page_elements.left_menu import LeftMenu


class UserPage(BasePage):
    """Class for the user page."""
    __SIGN_IN_BTN = (By.CSS_SELECTOR, "button.btn.btn-outline-white.header_signin")
    __USER_FULL_NAME = (By.CSS_SELECTOR, ".profile_name.display-4")

    def __init__(self, driver):
        super().__init__(driver)
        self.left_menu = LeftMenu(driver)

    def get_user_full_name(self, wait_time: int = 5):
        full_name = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.__USER_FULL_NAME))
        name, last_name = full_name.text.split()

        return name, last_name
