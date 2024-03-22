resistor_val = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

calculate_resistor = lambda c1, c2, c3: ((resistor_val[c1] * 10 + resistor_val[c2]) *
                                               (10 ** resistor_val[c3]))

color1, color2, color3 = input(), input(), input()

print(calculate_resistor(color1, color2, color3))
