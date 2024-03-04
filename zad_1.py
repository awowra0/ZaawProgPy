class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


caa = Student("Jan", [90,50,40,30])
cab = Student("Stefan", [10,60,50,75])
print(caa.is_passed())
print(cab.is_passed())
