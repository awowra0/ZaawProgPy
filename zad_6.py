def fun_f(la: list, lb: list) -> list:
    return [i**3 for i in set(la + lb)]
