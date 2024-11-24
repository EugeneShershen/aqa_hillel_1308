from assertpy import assert_that
from pytest import mark

from lesson_28.src.pages.user_page import UserPage
from lesson_28.tests.base_test import BaseTest


class TestMainPage(BaseTest):

    @mark.parametrize("method", (
            'sign_in',
            'sign_up'
    ))
    def test_registration(self, driver, fake_user, method):
        name, last_name, email, password = fake_user

        self.registration(driver, name, last_name, email, password, method)

        user_page = UserPage(driver)
        user_page.left_menu.select_profile()
        user_name, user_last_name = user_page.get_user_full_name()

        assert_that(user_name).is_equal_to(name)
        assert_that(user_last_name).is_equal_to(last_name)
