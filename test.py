
def is_simple(x):
    """Фукнция определения простоты"""
    global simples_list, composite_set

    if x in simples_list:              # проверка на вхождение в заране созданный список простых чисел
        return True
    elif x in composite_set:            # проверка на вхождение в заранее созданное множество составных чисел
        return False
    else:
        sum_number = 0
        for num in str(x):
            sum_number = int(num) + sum_number

        # проверка на базовые признаки делимости
        if (str(x)[-1] == "0") \
                or (str(x)[-1] == "5")\
                or (int(str(x)[-1]) % 2 == 0) \
                or (sum_number % 3 == 0):
            composite_set.add(x)
            return False

        # прямой тест простоты
        for i in range(2, x):
            if x % i == 0:
                composite_set.add(x)
                return False

        simples_list.append(x)
        return True


def simplifiers(x):
    """Возвращает множество (set) простых множителей своего аргумента"""
    multiply_arr = []
    while x != 1:
        for i in range(2, x + 1):
            if is_simple(i) and (x % i == 0):
                x = round(x / i)
                multiply_arr.append(i)
                continue
    # multiply_arr.sort()
    multiply_arr = set(multiply_arr)
    return multiply_arr


def gcd(x, y):
    """Проверка на существование хотя бы 1 общего делителя, кроме 1, из двух множеств простых делителей на вводе"""
    intersection = x.intersection(y)
    answer = 1
    if len(list(intersection)) > 1:
        answer = max(list(intersection))
    return answer


def rad(x):
    """Поиск радикала"""
    answer = 1
    for i in x:
        answer = answer * i
    return answer


def abc_check(a, b, c):
    """Проверка на abc совпадение"""
    sim_a = simplifiers(a)
    sim_b = simplifiers(b)
    sim_c = simplifiers(c)
    sim_abc = simplifiers(a * b * c)

    if rad(sim_abc) < c:
        if gcd(sim_a, sim_b) == gcd(sim_a, sim_c) == gcd(sim_b, sim_c) == 1:
            return True
    return False


if __name__ == "__main__":
    abc_combinations = []
    simples_list = [1, 2, 3, 5, 7]
    composite_set = set()
    combinations_checked = 0
    count = 0

    for b in range(3, 1000, 2):
        for a in range(1, b, 2):
            c = a + b
            combinations_checked = combinations_checked + 1
            # print(a, b, c, abc_check(a, b, c))
            if (c < 1000) and (abc_check(a, b, c)):
                abc_combinations.append([a, b, c])
                count += 1
            print("\r", a, b, c, "Совпадений:", count, "Комбинаций проврено:", combinations_checked, end="")

    n = 0
    for i in abc_combinations:
        n = n + 1
        print(n, ")", i)

