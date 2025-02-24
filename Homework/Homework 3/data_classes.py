import json

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, name, age, email, studentID):
        super().__init__(name, age, email)
        self.studentID = studentID

    def write_dict(self):
        return{
            "name": self.name,
            "age": self.age, 
            "email": self.email,
            "student ID": self.studentID

        }

    def save_to_json(cls, student_instance, file_name = "data.json"):
        try:    
            with open(file_name, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        
        data.append(student_instance.write_dict())

        with open(file_name, "w") as file:
            json.dump(data, file, indent = 4)

        print(f"{student_instance}'s data has been saved")