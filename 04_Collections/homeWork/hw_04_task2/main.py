# Семинар 4
# Домашняя работа
# Задача 2.
# В первом списке находится информация об ассортименте мороженного,
# во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.


def main():
    menuList = {"Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"}
    storeList = {"Сливочное", "Вафелька", "Сладкоежка"}
    print(f"Ice-cream in menu:{menuList}")
    print(f"Ice-cream in store: {storeList}")

    print("Ice-cream unavailable:")
    for item in menuList.difference(storeList):
        print(item, end=", ")


main()
