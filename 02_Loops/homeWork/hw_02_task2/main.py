# Семинар 2
# Домашняя работа
# Задача 2
# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def main():
    print("X  Y  Z  ¬(X ∧ Y) ∨ Z")
    rng = range(0, 2)
    for x in rng:
        for y in rng:
            for z in rng:
                print(f"{x}  {y}  {z}  {int((not (x and y)) or z)}")


main()
