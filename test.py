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

#taking user input
name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

#converting birth year to integer
birth_year = int(birth_year)

#calling the greet function
greet(name, birth_year)