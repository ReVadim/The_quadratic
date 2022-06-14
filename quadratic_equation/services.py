from math import sqrt


def quadratic_equation(a: float, b: float, c: float) -> any:
    """ Main equation. Returns the solution of the quadratic equation """

    if a == 0:
        if b == 0:
            return None
        else:
            return c * (-1) / b

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        return round(x1, 1), round(x2, 1)
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def solution_of_the_equation(data):
    """ solution of the quadratic equation """
    if not data:
        return 'Вы не предоставили данные'
    a = data['a']
    b = data['b']
    c = data['c']
    result = quadratic_equation(a, b, c)
    if not result:
        return {'status': 'Дискриминант меньше нуля, уравнение не имеет действительных решений.', 'result': None}
    if type(result) == float:
        return {'status': 'Уравнение имеет один корень', 'result1': result}
    else:
        return {'status': 'Уравнение имеет два корня', 'result2': result}
