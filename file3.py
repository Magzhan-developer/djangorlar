# student_stats.py
# Анализ оценок студентов

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def highest(self):
        return max(self.grades) if self.grades else None

    def lowest(self):
        return min(self.grades) if self.grades else None

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def best_student(self):
        return max(self.students, key=lambda s: s.average(), default=None)

    def average_score(self):
        if not self.students:
            return 0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

    def summary(self):
        print("Group summary:")
        for s in self.students:
            print(f"{s.name}: avg={s.average():.2f}, max={s.highest()}, min={s.lowest()}")
        print(f"Group average: {self.average_score():.2f}")
        best = self.best_student()
        if best:
            print(f"Top student: {best.name} ({best.average():.2f})")

if __name__ == "__main__":
    group = Group()
    group.add_student(Student("Alice", [80, 90, 85]))
    group.add_student(Student("Bob", [70, 60, 75]))
    group.add_student(Student("Charlie", [95, 92, 96]))
    group.summary()
