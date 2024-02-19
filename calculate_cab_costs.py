""" calculate_cab_costs

    This script calculates the cost of a cab ride,
    on the basis of the basic cost + the cost per km
"""


cost_base = 4.80
cost_per_km_under_5 = 1.90
cost_per_km_over_5 = 2.10

distance_km = int(input("\n Enter the distance you want to travel by cab: "))


if distance_km < 5: 
    cost_total = (cost_per_km_under_5 * distance_km) + cost_base
    print(f"\n {distance_km}km \n {cost_total}€ \n (basic rate & distance rate) \n")
else: 
    cost_total = (cost_per_km_over_5 * distance_km) + cost_base
    print(f"\n {distance_km}km \n {cost_total}€ \n (basic rate & distance rate) \n")