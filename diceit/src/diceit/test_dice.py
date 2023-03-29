import pytest
from dice import Dice, succsess_percentage_for_dice_roll

def test_dice_class():
    t6 = Dice(1, 6)
    isinstance(t6, Dice)


def test_calculate_cances_of_multiple_diece_roll():
    result = succsess_percentage_for_dice_roll(1, 1, 6, 1)
    assert result == 16.67

