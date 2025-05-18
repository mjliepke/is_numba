import pytest
from is_numba import *

test_data = [[2, True],
            [2.1, True],
            [-2.1, True],
            [None, False],
            [1E999, True],
            ["2.1", False],
            ["-2.1", False],
            [[1,2], False],
            [{"2":False}, False]]

@pytest.mark.parametrize("input,expected_output", test_data)
def test_is_number(input, expected_output:bool):
    test_result = is_numba(input)
    assert test_result == expected_output