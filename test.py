#This is a sample python file

#function to print name
def greet(name, birth_year):
    print(f"Hello, {name}!")
    print_age(birth_year)

#function to print age based on birth year
def print_age(birth_year):
    current_year=2026
    age = current_year - birth_year
    print(f"Age: {age}")

name = "KS"
birth_year = 1987
greet(name, birth_year)