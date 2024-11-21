from pytest import mark, raises
from assertpy import assert_that
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from lesson_27.src.pages.main_page import MainPage
from lesson_27.src.pages.wrong_format_page import WrongFormatPage
from lesson_27.data import urls, text_errors


class TestMainPage:
    """Class for testing the main page."""
    def is_main_page(self, driver: WebDriver):
        try:
            driver.find_element(By.CSS_SELECTOR, "input.track__form-group-input")
            return True
        except NoSuchElementException:
            return False

    @mark.parametrize("parcel_number, expected_text", [
        ("23443223442", text_errors.from_main_page),
        ("YT783625395OP", text_errors.from_wrong_format_page),
        ("0195692893641234", text_errors.from_wrong_format_page),
        ("utRo65782Gs321", text_errors.from_wrong_format_page),
        ("uBd8;1g@)27m,/jh05j", text_errors.from_wrong_format_page)
    ])
    def test_fill_parcel_number_negative(self, driver, parcel_number, expected_text):
        main_page = MainPage(driver)
        main_page.open(urls.main_page)
        main_page.fill_parcel_number(parcel_number)

        if self.is_main_page(driver):
            error_text = main_page.find_error_message()
            assert_that(error_text).is_equal_to(expected_text)

        else:
            wrong_format_page = WrongFormatPage(driver)
            wrong_format_page.open(f"{urls.wrong_format_page}{parcel_number}")
            error_text = wrong_format_page.find_error_message()

            assert_that(error_text).is_equal_to(expected_text)

    @mark.parametrize("parcel_number", ["12345", "ueqo541", "U$id[90>/e;173@"])
    def test_fill_parcel_number_short_number(self, driver, parcel_number):
        main_page = MainPage(driver)
        main_page.open(urls.main_page)
        main_page.fill_parcel_number(parcel_number)

        with raises(TimeoutException):
            main_page.find_error_message()
