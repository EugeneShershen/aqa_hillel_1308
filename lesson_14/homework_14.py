class Student:
    def __init__(self, first_name, last_name, age, average_score):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._average_score = average_score

    def print_info(self):
        print(f'First name: {self._first_name}\n'
              f'Last name : {self._last_name}\n'
              f'Age: {self._age}\n'
              f'Average score: {self._average_score}\n')

    def set_average_score(self, new_average_score):
        self._average_score = new_average_score


new_student = Student('Eugene', 'Shershen', 20, 81)

print('\nBefore change "average_score":\n')
new_student.print_info()

new_student.set_average_score(96)

print('\nAfter change "average_score":\n')
new_student.print_info()
