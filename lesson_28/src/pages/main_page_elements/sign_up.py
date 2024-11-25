from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.src.pages.base_page import BasePage


class SignUp(BasePage):
    """Class for the sign-up object."""
    __INPUT_NAME = (By.ID, "signupName")
    __INPUT_LAST_NAME = (By.ID, "signupLastName")
    __INPUT_EMAIL = (By.ID, "signupEmail")
    __INPUT_PASSWORD = (By.ID, "signupPassword")
    __INPUT_RE_PASSWORD = (By.ID, "signupRepeatPassword")
    __REGISTER_BTN = (By.CSS_SELECTOR, ".modal-footer .btn.btn-primary")

    def input_registration_info(self, name: str, last_name: str, email: str, password: str, wait_time: int = 5):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.__REGISTER_BTN))
        self.actions.fill(self.__INPUT_NAME, name)
        self.actions.fill(self.__INPUT_LAST_NAME, last_name)
        self.actions.fill(self.__INPUT_EMAIL, email)
        self.actions.fill(self.__INPUT_PASSWORD, password)
        self.actions.fill(self.__INPUT_RE_PASSWORD, password)

    def complete_registration(self):
        self.actions.click(self.__REGISTER_BTN)
