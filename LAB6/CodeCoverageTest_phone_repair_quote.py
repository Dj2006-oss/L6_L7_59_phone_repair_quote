
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# -------------------------------
# Tests for repair_quote()
# -------------------------------

def test_unknown_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)


def test_unknown_brand():
    with pytest.raises(ValueError):
        repair_quote("screen", "premium", False, False)


def test_flagship_screen_express():
    assert repair_quote("screen", "flagship", False, True) == 9100


def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600


def test_warranty_battery():
    assert repair_quote("battery", "flagship", True, False) == 300


def test_warranty_screen():
    assert repair_quote("screen", "budget", True, False) == 4600


def test_battery_express():
    assert repair_quote("battery", "budget", False, True) == 2300


# -------------------------------
# Tests for repair_days()
# -------------------------------

def test_no_technician():
    assert repair_days("battery", True, 0) == 3


def test_screen_not_in_stock():
    assert repair_days("screen", False, 2) == 6


def test_camera_not_in_stock():
    assert repair_days("camera", False, 2) == 6


def test_battery_not_in_stock():
    assert repair_days("battery", False, 2) == 3


def test_available_parts_and_technician():
    assert repair_days("camera", True, 1) == 1


# -------------------------------
# Tests for trade_in_value()
# -------------------------------

def test_invalid_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 10, False)


def test_invalid_age():
    with pytest.raises(ValueError):
        trade_in_value(10000, -1, False)


def test_phone_older_than_48_months():
    assert trade_in_value(10000, 50, False) == 0


def test_age_up_to_12_months():
    assert trade_in_value(10000, 12, False) == 6000


def test_age_up_to_24_months():
    assert trade_in_value(10000, 24, False) == 4000


def test_age_above_24_months():
    assert trade_in_value(10000, 36, False) == 2000


def test_cracked_screen():
    assert trade_in_value(10000, 36, True) == 1000
