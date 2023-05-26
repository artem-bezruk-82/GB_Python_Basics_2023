# Семинар 6
# Задача 4
# Имеется 1000 рублей.
# Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?


def main():
    budget = 1000

    bullPrice = 100
    cowsPrice = 50
    calfsPrice = 5

    bullsCount = budget // bullPrice
    cowsCount = budget // cowsPrice
    calfsCount = budget // calfsPrice

    for bulls in range(bullsCount + 1):
        for cows in range(cowsCount + 1):
            for calfs in range(calfsCount + 1):
                if bulls + cows + calfs == 100 and bulls * bullPrice + cows * cowsPrice + calfs * calfsPrice == 1000:
                    print(f"bulls: {bulls}; cows: {cows}; calfs: {calfs}")


main()
