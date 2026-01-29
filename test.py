from person import Person

name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

#converting birth year to integer
birth_year = int(birth_year)

#creating an instance of Person class
person1 = Person(name, birth_year)

#calling the greet function
person1.greet()