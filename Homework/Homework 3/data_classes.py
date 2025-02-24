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
        # Return a dictionary representing the student instance
        return {
            "name": self.name,
            "age": self.age, 
            "email": self.email,
            "student ID": self.studentID
        }

    @classmethod
    def save_to_json(cls, student_instance, file_name="student_data.json"):
        # Try reading the existing data from the file
        try:    
            with open(file_name, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # Start with an empty list if no file exists or file is empty

        # Append the student data to the list
        data.append(student_instance.write_dict())

        # Write the updated data back to the file
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Data for {student_instance.name} has been saved.")

