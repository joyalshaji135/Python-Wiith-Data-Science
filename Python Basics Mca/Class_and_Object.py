class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

    def update_major(self, new_major):
        self.major = new_major

    def is_adult(self):
        return self.age >= 18

def get_student_details():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    major = input("Enter Student Major: ")
    
    return Student(student_id, name, age, major)

def main():
    
    student = get_student_details()

    
    print("\nStudent Details:")
    print(student)
        
    
    if student.is_adult():
        print(f"{student.name} is an adult.")
    else:
        print(f"{student.name} is not an adult.")

if __name__ == "__main__":
    main()
