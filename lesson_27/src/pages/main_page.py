from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_27.src.pages.base_page import BasePage


class MainPage(BasePage):
    """Class for the main page."""
    __INPUT_PARCEL_NUMBER = (By.XPATH, "//input[@class='track__form-group-input']")
    __BUTTON_PARCEL_NUMBER = (By.ID, "np-number-input-desktop-btn-search-en")
    __SPAN_ERROR_ELEMENT = (By.CSS_SELECTOR, "div#np-number-input-desktop-message-error-message span")

    def fill_parcel_number(self, number: str):
        self.actions.fill(self.__INPUT_PARCEL_NUMBER, number)
        self.actions.click(self.__BUTTON_PARCEL_NUMBER)

    def find_error_message(self, wait_time: int = 5):
        span = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(self.__SPAN_ERROR_ELEMENT))

        return span.text
