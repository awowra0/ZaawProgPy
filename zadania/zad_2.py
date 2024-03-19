import zadania.Student as stud
import zadania.Library as lib
import zadania.Employee as emp
import zadania.Book as bk
import zadania.Order as orde


def fun_2():
    caa = stud.Student("Jan", [90, 50, 40, 30])
    cab = stud.Student("Stefan", [10, 60, 50, 75])
    cbl1 = lib.Library("Katowice", "Katowicka 24", 987, "10-18", 301857432)
    cbl2 = lib.Library("Chorzów", "Kościelna 19", 990, "9-17", 301858555)
    cbb1 = bk.Book(cbl1, "13.12.2011", "Jan", "Kowalski", 98)
    cbb2 = bk.Book(cbl1, "04.06.1993", "Antoni", "Bartoszeski", 134)
    cbb3 = bk.Book(cbl2, "05.10.2002", "Stefan", "Baner", 291)
    cbb4 = bk.Book(cbl2, "29.01.2021", "Renata", "Altana", 236)
    cbb5 = bk.Book(cbl1, "01.01.2001", "Andrzej", "Dyg", 65)
    cbe1 = emp.Employee("Janusz", "Palindrom", "13.11.2020", "08.07.1974",
                        "Katowice", "Bogucicka 23", 1031, 777999000)
    cbe2 = emp.Employee("Irena", "Jankowska", "17.06.2017", "13.04.1994",
                        "Chorzów", "Katowicka 9", 1001, 777888999)
    cbe3 = emp.Employee("Dariusz", "Król", "21.02.2022", "10.10.1990",
                        "Katowice", "Padereckiego 40", 1040, 890890890)
    cbo1 = orde.Order(cbe1, caa, [cbb1, cbb2], "28.02.2024")
    cbo2 = orde.Order(cbe2, cab, [cbb3], "31.01.2024")
    print(cbo1)
    print(cbo2)
