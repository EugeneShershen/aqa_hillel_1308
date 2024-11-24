from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.src.pages.base_page import BasePage


class LeftMenu(BasePage):
    """Class for the left menu of user page."""
    __PROFILE_BTN = (By.CSS_SELECTOR, ".btn.btn-white.btn-sidebar.sidebar_btn.-profile")

    def select_profile(self, wait_time: int = 5):
        btn = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.__PROFILE_BTN))
        btn.click()
