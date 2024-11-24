from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.src.pages.base_page import BasePage


class SignIn(BasePage):
    """Class for the sign in object."""
    __REGISTRATION_BTN = (By.CSS_SELECTOR, ".modal-footer.d-flex.justify-content-between .btn.btn-link")

    def press_registration_btn(self, wait_time: int = 5):
        btn = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.__REGISTRATION_BTN))
        btn.click()
