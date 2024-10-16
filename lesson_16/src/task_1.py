import inspect


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def attributes(self):
        atr_list = []

        for i in inspect.getmembers(self):

            if not i[0].startswith('_'):

                if not inspect.ismethod(i[1]):
                    atr_list.append(i[0])

        return atr_list


class Manager(Employee):

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)
        self.team_size = team_size
