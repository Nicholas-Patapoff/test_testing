import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from backend.utils import hash_password, paginate, timestamp


def test_timestamp_is_int():
    assert isinstance(timestamp(), int)


def test_hash_password_returns_hex():
    result = hash_password("secret")
    assert len(result) == 64
    assert all(c in "0123456789abcdef" for c in result)


def test_paginate_first_page():
    items = list(range(10))
    assert paginate(items, 1, 3) == [0, 1, 2]


def test_paginate_last_page():
    items = list(range(10))
    assert paginate(items, 4, 3) == [9]
