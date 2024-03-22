class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

# Example usage:
if __name__ == "__main__":
    # Create a Student object
    student1 = Student(student_id=1, name="John Doe", age=18, grade="A")

    # Print the student object
    print(student1)

    # Convert the student object to a dictionary
    student_dict = student1.to_dict()
    print(student_dict)
