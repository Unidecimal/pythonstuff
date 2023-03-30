from diceit import dice

def test_dice_class():
    t6 = dice.Dice(6, 1)
    isinstance(t6, dice.Dice)

def test_calculate_cances_of_multiple_diece_roll():
    result = dice.succsess_percentage_for_dice_roll(1, 1, 6, 1)
    assert result == 16.67



