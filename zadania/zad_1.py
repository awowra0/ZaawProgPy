import zadania.Student

def fun_1():
    caa = zadania.Student.Student("Jan", [90, 50, 40, 30])
    cab = zadania.Student.Student("Stefan", [10, 60, 50, 75])
    print(caa.is_passed())
    print(cab.is_passed())
