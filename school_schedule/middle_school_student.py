from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        return f"{super().summary()} Transportation: {self.gets_transportation}"
