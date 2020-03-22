def simplifier(x):
    """Возвращает массив простых множителей своего аргумента"""

    multiply_arr = []
    while x != 1:
        for i in range(2, x + 1):
            if is_simple(i) and (x % i == 0):
                x = round(x / i)
                multiply_arr.append(i)
                continue
    multiply_arr.sort()
    return multiply_arr


def is_simple(x):
    """Фукнция определения простоты"""
    global simples_list

    if x in simples_list:
        return True
    else:
        sum_number = 0
        for num in str(x):
            sum_number = int(num) + sum_number

        # проверка на базовые признаки делимости
        if (str(x)[-1] == "0") \
                or (str(x)[-1] == "5")\
                or (int(str(x)[-1]) % 2 == 0) \
                or (sum_number % 3 == 0):
            return False

        # прямой тест простоты
        for i in range(2, x):
            if x % i == 0:
                return False

        simples_list.append(x)
        return True


simples_list = [1, 2, 3, 5, 7]

x = int(input("Введите число: "))

print(simplifier(x))