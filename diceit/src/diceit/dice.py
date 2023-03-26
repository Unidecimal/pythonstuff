import math

# Antal tärningar
n = 1

# Antal "framgångar"
k = 1

# Totala antal sidor på tärningen
tot_sides = 6

# Antal sidor på tärningen som ger en "framgång"
successes_sides = 1

# Beräkna sannolikheten med hjälp av binomialfördelningen
prob = sum(
    [math.comb(n, i) * (successes_sides/tot_sides)**i * (1-(successes_sides/tot_sides))**(n-i) 
     for i in range(k, n+1)]
    )

print(f"Sannolikhet att slå över {tot_sides - successes_sides} på minst {k} av {n} tärningar: {prob:.2%}")
