# Семинар 4
# Задание 2
# На вход подаются два числа. Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел.

def main():
    valA = 6
    valB = 2
    result = get_sum_dif_prod_div(valA, valB)
    print(f"sum = {result[0]}; dif = {result[1]}; prod = {result[2]}; div = {result[3]}; ")
    print_result(*result)


def print_result(sum, dif, prod, div):
    print(f"sum = {sum}; dif = {dif}; prod = {prod}; div = {div}; ")


def get_sum_dif_prod_div(valA, valB):
    return valA+valB, valA-valB, valA*valB, valA/valB


main()
