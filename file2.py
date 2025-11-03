# file_manager.py
# Утилита для чтения, записи и анализа текстовых файлов

import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_lines(self, lines):
        with open(self.filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")

    def read_lines(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError("File not found!")
        with open(self.filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]

    def count_lines(self):
        lines = self.read_lines()
        return len(lines)

    def count_words(self):
        lines = self.read_lines()
        return sum(len(line.split()) for line in lines)

    def append_line(self, text):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")

if __name__ == "__main__":
    manager = FileManager("test.txt")
    manager.write_lines(["Hello world", "Python is fun", "Git worktree is cool"])
    print("Total lines:", manager.count_lines())
    print("Total words:", manager.count_words())
    manager.append_line("This is an appended line.")
    print("Lines after append:", manager.count_lines())
    print("practice-6-main-duplicate-3 changes")
    print("adding change to file2.py")
