from pytest import mark
from assertpy import assert_that

from lesson_24.src.user import User
from lesson_24.data.cars_data import cars_db


def sorted_limited_cars(cars, sort_by, limit):
    sorted_cars = sorted(cars.values(), key=lambda x: x.get(sort_by, 0) if sort_by else x['brand'])
    limited_cars = sorted_cars[:int(limit)] if limit else sorted_cars

    return limited_cars


class TestGetCars:
    @mark.parametrize('username, password, text', [
        ('test_user', 'test_pass', None),
        ('', '', 'Аутентифікація не пройшла!'),
        (34, -20, 'Неправильне ім\'я користувача або пароль!'),
        (None, None, 'Неправильне ім\'я користувача або пароль!')
    ])
    def test_get_token(self, username, password, text, log):
        result = User(log).get_token(username, password)

        if result['status_code'] == 200:
            assert_that(result['access_token']).is_not_equal_to(None)

        else:
            assert_that(result['message']).is_equal_to(text)

    @mark.parametrize('sort_by, limit', [
        (None, None),
        ('brand', 5),
        ('year', -10),
        ('engine_volume', 19),
        ('price', 2)
    ])
    def test_get_cars(self, log, authenticate, sort_by, limit):
        expected_result = sorted_limited_cars(cars_db, sort_by, limit)

        result = User(log).get_cars(authenticate, sort_by, limit)

        assert_that(result).is_equal_to(expected_result)
