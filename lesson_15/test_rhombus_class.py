import pytest
from pytest import mark

from homework_15 import Rhombus


class TestRhombusClass:
    list_data_test = [12, 376, 0, -9, 3.5]

    @mark.parametrize('side', list_data_test)
    def test_side_attribute(self, side):
        corner_a = 75

        if side > 0:
            sample_rhombus = Rhombus(side, corner_a)

            expected_result = side
            result = sample_rhombus.side
        else:
            with pytest.raises(ValueError) as info:
                Rhombus(side, corner_a)

            expected_result = 'Side must be more than 0 cm'
            result = str(info.value)

        assert result == expected_result

    @mark.parametrize('corner_a', list_data_test)
    def test_corner_a_attribute(self, corner_a):
        side = 20

        if 0 < corner_a < 180:
            sample_rhombus = Rhombus(side, corner_a)

            expected_result = corner_a
            result = sample_rhombus.corner_a
        else:
            with pytest.raises(ValueError) as info:
                Rhombus(side, corner_a)

            expected_result = 'Corner "α" must be more than 0° and less than 180°'
            result = str(info.value)

        assert result == expected_result

    def test_print_result(self):
        side = 45
        corner_a = 93
        corner_b = 87
        expected_result = (f'Side: {side} cm\n'
                           f'Corner "α": {corner_a}°\n'
                           f'Corner "β": {corner_b}°')

        sample_rhombus = Rhombus(side, corner_a)
        result = sample_rhombus.__str__()

        assert result == expected_result
