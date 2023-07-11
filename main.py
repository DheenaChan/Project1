# Employee Management

import mysql.connector

# Establish a connection to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DheenaChan@333",
    database="employee_management"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to add a new employee


def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    query = "INSERT INTO employees (e_name, e_age, e_position, e_salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)

    cursor.execute(query, values)
    db.commit()
    print("Employee added successfully.")

# Function to retrieve employee information


def retrieve_employee():
    employee_id = int(input("Enter employee ID: "))

    query = "SELECT * FROM employees WHERE e_id = %s"
    values = (employee_id,)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        print("Employee ID:", result[0])
        print("Name:", result[1])
        print("Age:", result[2])
        print("Position:", result[3])
        print("Salary:", result[4])
    else:
        print("Employee not found.")

# Function to update employee information


def update_employee():
    employee_id = int(input("Enter employee ID: "))

    query = "SELECT * FROM employees WHERE e_id = %s"
    values = (employee_id,)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        print("Current Employee Information:")
        print("Name:", result[1])
        print("Age:", result[2])
        print("Position:", result[3])
        print("Salary:", result[4])

        name = input("Enter new name (or press enter to skip): ")
        age = input("Enter new age (or press enter to skip): ")
        position = input("Enter new position (or press enter to skip): ")
        salary = input("Enter new salary (or press enter to skip): ")

        updates = []
        if name:
            updates.append(f"e_name = '{name}'")
        if age:
            updates.append(f"e_age = {age}")
        if position:
            updates.append(f"e_position = '{position}'")
        if salary:
            updates.append(f"e_salary = {salary}")

        if updates:
            set_clause = ", ".join(updates)
            query = f"UPDATE employees SET {set_clause} WHERE e_id = %s"
            values = (employee_id,)
            cursor.execute(query, values)
            db.commit()
            print("Employee information updated successfully.")
        else:
            print("No updates provided.")
    else:
        print("Employee not found.")

# Function to delete an employee


def delete_employee():
    employee_id = int(input("Enter employee ID: "))

    query = "DELETE FROM employees WHERE e_id = %s"
    values = (employee_id,)

    cursor.execute(query, values)
    db.commit()
    print("Employee deleted successfully.")

# Function to list all employees


def list_employees():
    query = "SELECT * FROM employees"

    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        for employee in result:
            print("Employee ID:", employee[0])
            print("Name:", employee[1])
            print("Age:", employee[2])
            print("Position:", employee[3])
            print("Salary:", employee[4])
            print("---------------------------")
    else:
        print("No employees found.")

# Main program loop


while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Retrieve Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. List Employees")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        retrieve_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        list_employees()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection

cursor.close()
db.close()
# End
