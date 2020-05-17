import datetime
from math import sqrt


def is_simple(x):
    """Фукнция определения простоты"""
    global simples_set

    if x in simples_set:              # проверка на вхождение в заране созданное множество простых чисел
        return True
    else:
        # sum_number = 0
        # for num in str(x):
        #     sum_number = int(num) + sum_number

        # проверка на базовые признаки делимости
        # if (str(x)[-1] == "0") \
        #         or (str(x)[-1] == "5")\
        #         or (int(str(x)[-1]) % 2 == 0) \
        #         or (sum_number % 3 == 0):
        #     return False

        int_sqrt_x = int(sqrt(x) + 1)

        # прямой тест простоты
        for i in simples_set:
            if i <= int_sqrt_x:
                if x % i == 0:
                    return False

        simples_set.add(x)
        return True


def simplifiers(x: int):
    """Возвращает множество (set) простых множителей своего аргумента"""
    multiply_set = {1}
    while x != 1:
        for i in range(2, x + 1):
            if is_simple(i) and (x % i == 0):
                x = round(x / i)
                multiply_set.add(i)
                continue
    return multiply_set


def gcd(x, y: set):
    """Проверка на существование хотя бы 1 общего делителя, кроме 1, из двух множеств простых делителей на вводе"""
    intersection = x.intersection(y)
    answer = max(list(intersection))
    return answer


def rad(x: set):
    """Поиск радикала"""
    answer = 1
    for i in x:
        answer = answer * i
    return answer


def abc_check(a, b, c: int):
    """Проверка на abc совпадение"""
    sim_a = simplifiers(a)
    sim_b = simplifiers(b)
    sim_c = simplifiers(c)
    sim_abc = simplifiers(a * b * c)

    if rad(sim_abc) < c:
        if gcd(sim_a, sim_b) == gcd(sim_a, sim_c) == gcd(sim_b, sim_c) == 1:
            return True
    return False


abc_combinations = []
simples_set = {2, 3, 5, 7}
combinations_checked = 0
count = 0
sum_c = 0
print()

if __name__ == '__main__':
    start = datetime.datetime.now()
    for b in range(3, 1000, 1):
        for a in range(1, b, 1):
            c = a + b
            combinations_checked = combinations_checked + 1
            print("\rКомбинаций проверено: " + str(combinations_checked), end="")
            if (c < 1000) and (abc_check(a, b, c)):
                abc_combinations.append([a, b, c])
                count += 1
                sum_c = sum_c + c
                time_for_count = datetime.datetime.now()
                time_elapsed = time_for_count - start
                print("\r"+str(count)+")", a, b, c, "Комбинаций проврено:"+str(combinations_checked)+","
                      , "sum_c =", sum_c, ". "+str(time_elapsed.seconds)+" сек")


    n = 0
    for i in abc_combinations:
        n = n + 1
        print(n, ")", i)

