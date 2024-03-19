burger_prices = min(int(input()) for _ in range(3))
drink_prices = min(int(input()) for _ in range(2))

set_menu_price = burger_prices + drink_prices - 50

print(set_menu_price)
