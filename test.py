
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


def gcd(x, y):
    """Поиск наибольшего общего делителя"""
    x = set(simplifier(x))
    y = set(simplifier(y))
    intersection = x.intersection(y)
    answer = 1
    for i in intersection:
        answer = answer * i
    return answer


def rad(x):
    """Поиск радикала"""
    answer = 1
    for i in set(simplifier(x)):
        answer = answer * i
    return answer


def abc_check(a, b, c):
    """Проверка на abc совпадение"""
    if gcd(a, b) == gcd(a, c) == gcd(b, c) == 1:
        if rad(a * b * c) < c:
            return True
    return False


if __name__ == "__main__":
    abc_combinations = []
    simples_list = [1, 2, 3, 5, 7]

    count = 0

    for b in range(1, 1000, 2):
        for a in range(1, b, 2):
            c = a + b
            # print(a, b, c, abc_check(a, b, c))
            if (c < 1000) and (abc_check(a, b, c)):
                abc_combinations.append([a, b, c])
                count += 1
            print("\r", a, b, c, "Совпадений:", count, end="")

    n = 0
    for i in abc_combinations:
        n = n + 1
        print(n, ")", i)

