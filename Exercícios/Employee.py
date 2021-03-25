
class Employee:

    def __init__(self, first_name, surname, annual_salary):
        self.first_name = first_name
        self.surname = surname
        self.annual_salary = annual_salary

    def give_raise(self, increase=5000):
        self.annual_salary += increase

    def show_person(self):
        print(f'{self.first_name} {self.surname}, ${self.annual_salary}.')


person = Employee('Danilo', 'Jorge', 5000)
person.give_raise()
person.show_person()
