import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.ledger.ledger import calculate_balance


def test_balance_basic():
    assert calculate_balance([100, -50]) == 50

def test_balance_basic():
    assert calculate_balance([100, -50]) == 50