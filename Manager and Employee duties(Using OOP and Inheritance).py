# I am a manager and i wanna hire a person, the below code will explain his different roles in the organisation
# i will use OOP(Object oriented programming to write this code)
# i will use the inheritance method to differenciate the different kind of roles

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        """show basic details of the person"""
        print(f"name:{self.name}")
        print(f"age:{self.age}")

class Employee:
    def __init__(self,name,age,job_title,salary):
        self.name = name
        self.age = age
        self.job_title = job_title
        self.salary = salary

    def show_details(self):
        print(f"job title:{self.job_title}")
        print(f"salary:{self.salary}")

    def perform_duties(self):
        """show the duties of an employee"""
        print(f"{self.name}perfoms tasks related to{self.job_title}")

class Manager(Person):
    def __init__(self,name,age,department,team_size):
        super().__init__(name,age)
        self.department = department
        self.team_size = team_size

    def show_details(self):
        """show details of a specific manager"""
        super().show_details
        print(f"department:{self.department}")
        print(f"team size:{self.team_size}")

    def manage_team(self):
        """show managers responsibility"""
        print(f"{self.name}manages a team of {self.team_size}in the department of{self.department}")


if __name__ == "__main__":
    employee = Employee(name= "Alice",age = 30,job_title="software developer",salary=75000 )
    manager = Manager(name ="vincent",age = 29,department="IT",team_size=10 )

    print("Employee details")
    employee.show_details()
    employee.perform_duties()

    print("\nManager details")
    manager.show_details()
    manager.manage_team()


