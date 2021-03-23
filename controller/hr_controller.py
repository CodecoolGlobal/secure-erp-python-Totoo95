import sys, os
sys.path.append(os.getcwd())
from datetime import date
from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_table(hr.content)


def add_employee():
    new_employee = []
    id = hr.get_id()
    name = input("Enter name: ")
    birthdate = input("Enter birthate [YYYY-MM-DD]: ")
    department = input("Enter department: ")
    clearence = input("Clearence level: ")
    
    new_employee.append(id)
    new_employee.append(name)
    new_employee.append(birthdate)
    new_employee.append(department)
    new_employee.append(clearence)
    hr.content.append(new_employee)
    hr.write_to_file(hr.content)




def update_employee():
    id = input("Enter customer id: ")
    for customer in hr.content:
        if customer[0] == id:
            for index, data in enumerate(customer):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    customer[index] = new_data
    
    hr.write_to_file(hr.content)


def delete_employee():
    id = input("Enter customer id: ")
    for index, customer in enumerate(hr.content):
        if customer[0] == id:
            hr.content.pop(index)
    hr.write_to_file(hr.content)



def get_oldest_and_youngest():
    birthdays = {}
    hr.content.pop(0)
    for customers in hr.content:
        birthdays.update({customers[0]: customers[2]})
    year, month, day = 10000, 13, 32
    for key, value in birthdays.items():
        if int(value.split("-")[0]) < year:
            year = int(value.split("-")[0])
            oldest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) < month:
            month = int(value.split("-")[1])
            oldest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) == month and int(value.split("-")[2]) < day:
            day = int(value.split("-")[2])
            oldest_id = key
    
    year, month, day = 0, 0, 0
    for key, value in birthdays.items():
        if int(value.split("-")[0]) > year:
            year = int(value.split("-")[0])
            youngest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) > month:
            month = int(value.split("-")[1])
            youngest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) == month and int(value.split("-")[2]) > day:
            day = int(value.split("-")[2])
            youngest_id = key
    
    for customer in hr.content:
        if customer[0] == oldest_id:
            oldest_id += " " + customer[1] + " " + customer[2]
    
    for customer in hr.content:
        if customer[0] == youngest_id:
            youngest_id += " " + customer[1] + " " + customer[2]
    
    print("Oldest: " + oldest_id)
    print("Youngest: " + youngest_id)



def get_average_age():
    today = str(date.today()).split("-")
    birthdates = []
    hr.content.pop(0)
    for customer in hr.content:
        birthdates.append(customer[2])
    sum_age = 0
    for birth in birthdates:
        birth = birth.split("-")
        age = int(today[0]) - int(birth[0])
        if int(today[1]) == int(birth[1]) and int(today[2]) == int(birth[2]):
            sum_age += age
            continue
        elif int(today[1]) <= int(birth[1]):
            if int(today[2]) < int(birth[2]) and int(today[1]) == int(birth[1]):
                age -= 1
                sum_age += age
                continue
            age -= 1
        sum_age += age
    
    avg_age = float(sum_age/len(birthdates))
    print(avg_age)

get_average_age()


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
