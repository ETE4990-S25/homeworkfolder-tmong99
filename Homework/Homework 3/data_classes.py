import json

class Person (object):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, name, age, email, studentID):
        super().__init__(self, name, age, email)
        self.studentID = studentID

    def write_dict(self):
        return{
            "name": self.name,
            "age": self.age, 
            "email": self.email,
            "student ID": self.studentID

        }

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.write_dict(), file, indent = 4)