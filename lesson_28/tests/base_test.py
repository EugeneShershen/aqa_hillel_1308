from selenium.webdriver.remote.webdriver import WebDriver

from lesson_28.src.pages.main_page import MainPage


class BaseTest:

    def registration(self, driver: WebDriver, name, last_name, email, password, method):
        main_page = MainPage(driver)
        main_page.open()

        if method == "sign_in":
            main_page.click_sign_in_btn()
            main_page.sign_in.press_registration_btn()
        elif method == "sign_up":
            main_page.click_sign_up_btn()

        main_page.sign_up.input_registration_info(name, last_name, email, password)
        main_page.sign_up.complete_registration()
