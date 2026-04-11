import json

# Load data if exists
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except:
    students = {}


def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)


def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists!")
        return

    try:
        age = int(input("Enter student age: "))
    except:
        print("Invalid age!")
        return

    course = input("Enter student course: ").strip()

    students[name] = {"age": age, "course": course}
    save_data()

    print(f"Student '{name}' added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for name, details in students.items():
        print(f"Name: {name}, Age: {details['age']}, Course: {details['course']}")


def update_student():
    name = input("Enter student name to update: ").strip()

    if name not in students:
        print("Student not found.")
        return

    print("Leave field empty to keep old value")

    age_input = input("Enter new age: ")
    course = input("Enter new course: ").strip()

    if age_input:
        try:
            students[name]['age'] = int(age_input)
        except:
            print("Invalid age!")

    if course:
        students[name]['course'] = course

    save_data()
    print(f"Student '{name}' updated successfully.")


def delete_student():
    name = input("Enter student name to delete: ").strip()

    if name not in students:
        print("Student not found.")
        return

    del students[name]
    save_data()

    print(f"Student '{name}' deleted successfully.")


# Main Menu
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")