class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    #function to print name
    def greet(self):
        print(f"Hello, {self.name}!")
        self.print_age()

    #function to print age based on birth year
    def print_age(self):
        current_year=2026
        age = current_year - self.birth_year
        print(f"Age: {age}")

