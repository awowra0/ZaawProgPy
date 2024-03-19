import zadania.Student as stud
import zadania.Employee as emp
import zadania.Book as bk


class Order:
    def __init__(self, employee: emp.Employee, student: stud.Student, books: list,
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
