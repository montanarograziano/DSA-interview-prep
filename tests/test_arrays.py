"""Test module for arrays."""

from typing import Literal

import pytest

from src.arrays import binary_search


@pytest.mark.parametrize(
    "array, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, False),
        ([1, 2, 3, 4, 5], 0, False),
        ([1, 2, 3, 4, 5], 1, True),
        ([1, 2, 3, 4, 5], 5, True),
        ([1, 2, 3, 4, 5], 2, True),
    ],
)
def test_binary_search(
    array: list[int],
    target: Literal[3] | Literal[6] | Literal[0] | Literal[1] | Literal[5] | Literal[2],
    expected: bool,
):
    assert binary_search(array, target) == expected
