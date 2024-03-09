class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka znajdująca się w mieście {self.city}, " +
                f"na ulicy {self.street}. Godziny otwarcia: " +
                f"{self.open_hours}. Telefon: {self.phone}. " +
                f"Zip code: {self.zip_code}.")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik {self.first_name} {self.last_name}, " +
                f"zatrudniony {self.hire_date}. Data urodzenia: " +
                f"{self.birth_date}. Adres: {self.city}, " +
                f"{self.street}. Telefon {self.phone}. " +
                f"Zip code: {self.zip_code}.")


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka z {self.library} Opublikowana " +
                f"{self.publication_date}, jej autorem jest " +
                f"{self.author_name} {self.author_surname}. " +
                f"Zawiera {self.number_of_pages} stron.")


class Order:
    def __init__(self, employee: Employee, student: Student, books: list,
                 order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f"Zamówienie złożone przez {self.student.name}, dnia " +
                f"{self.order_date}, na książki: " +
                f"{[str(i) for i in self.books]} " +
                f"Zamówienie jest realizowane przez {self.employee}")


caa = Student("Jan", [90, 50, 40, 30])
cab = Student("Stefan", [10, 60, 50, 75])
cbl1 = Library("Katowice", "Katowicka 24", 987, "10-18", 301857432)
cbl2 = Library("Chorzów", "Kościelna 19", 990, "9-17", 301858555)
cbb1 = Book(cbl1, "13.12.2011", "Jan", "Kowalski", 98)
cbb2 = Book(cbl1, "04.06.1993", "Antoni", "Bartoszeski", 134)
cbb3 = Book(cbl2, "05.10.2002", "Stefan", "Baner", 291)
cbb4 = Book(cbl2, "29.01.2021", "Renata", "Altana", 236)
cbb5 = Book(cbl1, "01.01.2001", "Andrzej", "Dyg", 65)
cbe1 = Employee("Janusz", "Palindrom", "13.11.2020", "08.07.1974",
                "Katowice", "Bogucicka 23", 1031, 777999000)
cbe2 = Employee("Irena", "Jankowska", "17.06.2017", "13.04.1994",
                "Chorzów", "Katowicka 9", 1001, 777888999)
cbe3 = Employee("Dariusz", "Król", "21.02.2022", "10.10.1990",
                "Katowice", "Padereckiego 40", 1040, 890890890)
cbo1 = Order(cbe1, caa, [cbb1, cbb2], "28.02.2024")
cbo2 = Order(cbe2, cab, [cbb3], "31.01.2024")
print(cbo1)
print(cbo2)
