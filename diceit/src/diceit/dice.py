import math


def the_old_code():
    # Antal tärningar
    n = 1

    # Antal "framgångar"
    k = 1

    # Totala antal sidor på tärningen
    dice_tot_sides = 6

    # Antal sidor på tärningen som ger en "framgång"
    successes_sides = 1

    # Beräkna sannolikheten med hjälp av binomialfördelningen
    prob = sum(
        [math.comb(n, i) * (successes_sides/dice_tot_sides)**i * (1-(successes_sides/dice_tot_sides))**(n-i)
        for i in range(k, n+1)]
        )

    print(f"Sannolikhet att slå över {dice_tot_sides - successes_sides} på minst {k} av {n} tärningar: {prob:.2%}")

def succsess_percentage_for_dice_roll(dice_n: int, success_dice_n: int, dice_tot_sides: int, successes_sides: int) -> int:

    # Number of dices
    #dice_n = 1

    # Number of succsesses needed
    #success_dice_n = 1

    # Total number of sides on the dice
    #dice_tot_sides = 6

    # The number of sides that result in succsess
    #successes_sides = 1

    # Calculate the probability using the binomial distribution
    prob = sum(
        [math.comb(dice_n, i) * (successes_sides/dice_tot_sides)**i * (1-(successes_sides/dice_tot_sides))**(dice_n-i)
        for i in range(success_dice_n, dice_n+1)]
        )

    return round(prob * 100, 2)
class Dice:
    pass
