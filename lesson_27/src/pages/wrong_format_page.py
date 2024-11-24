from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_27.src.pages.base_page import BasePage


class WrongFormatPage(BasePage):
    """Class for page while entering parcel number in wrong format."""
    __DIV_ERROR_ELEMENT = (By.CSS_SELECTOR, "div.tracking__error-text")

    def find_error_message(self, wait_time: int = 5):
        div = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(self.__DIV_ERROR_ELEMENT))

        return div.text
