
import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# =====================================
# 1. Tests for repair_quote()
# =====================================

def test_invalid_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)


def test_invalid_brand():
    with pytest.raises(ValueError):
        repair_quote("screen", "premium", False, False)


def test_flagship():
    assert repair_quote("screen", "flagship", False, False) == 8600


def test_budget():
    assert repair_quote("battery", "budget", False, False) == 1800


def test_screen_part():
    assert repair_quote("screen", "budget", False, False) == 4600


def test_non_screen_part():
    assert repair_quote("camera", "budget", False, False) == 2800


def test_warranty_non_screen():
    assert repair_quote("battery", "budget", True, False) == 300


def test_warranty_screen():
    assert repair_quote("screen", "budget", True, False) == 4600


def test_no_warranty():
    assert repair_quote("battery", "budget", False, False) == 1800


def test_express_service():
    assert repair_quote("battery", "budget", False, True) == 2300


def test_normal_service():
    assert repair_quote("battery", "budget", False, False) == 1800


# =====================================
# 2. Tests for repair_days()
# =====================================

def test_no_technician():
    assert repair_days("battery", True, 0) == 3


def test_technician_available():
    assert repair_days("battery", True, 1) == 1


def test_parts_in_stock():
    assert repair_days("screen", True, 1) == 1


def test_screen_not_in_stock():
    assert repair_days("screen", False, 1) == 6


def test_camera_not_in_stock():
    assert repair_days("camera", False, 1) == 6


def test_battery_not_in_stock():
    assert repair_days("battery", False, 1) == 3


# =====================================
# 3. Tests for trade_in_value()
# =====================================

def test_invalid_original_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 10, False)


def test_invalid_age():
    with pytest.raises(ValueError):
        trade_in_value(10000, -1, False)


def test_both_invalid_inputs():
    with pytest.raises(ValueError):
        trade_in_value(0, -1, False)


def test_age_above_48():
    assert trade_in_value(10000, 50, False) == 0


def test_age_within_12_months():
    assert trade_in_value(10000, 12, False) == 6000


def test_age_within_24_months():
    assert trade_in_value(10000, 24, False) == 4000


def test_age_above_24_months():
    assert trade_in_value(10000, 36, False) == 2000


def test_cracked_screen():
    assert trade_in_value(10000, 36, True) == 1000


def test_screen_not_cracked():
    assert trade_in_value(10000, 36, False) == 2000
