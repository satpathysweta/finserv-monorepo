import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.ledger.ledger import calculate_balance


def test_balance_basic():
    assert calculate_balance([100, -50]) == 50




def test_balance_empty_list():
    assert calculate_balance([]) == 0


def test_balance_negative_result():
    assert calculate_balance([-100, 20, -50]) == -130


def test_balance_all_negative():
    assert calculate_balance([-10, -20, -30]) == -60


def test_balance_with_zero():
    assert calculate_balance([0, 100, -50, 0]) == 50
