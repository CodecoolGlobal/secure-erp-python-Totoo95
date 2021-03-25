import sys, os
sys.path.append(os.getcwd())
from datetime import date, datetime
from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_table(hr.get_content_from_file())


def add_employee():
    hr.add_employee()


def update_employee():
    id = view.get_input("Enter employee id")
    hr.update_emmployee(id)


def delete_employee():
    id = view.get_input("Enter employee id")
    hr.delete_employee(id)


def get_oldest_and_youngest():
    view.print_general_results(hr.get_oldest_and_youngest(), "Oldest and youngest: ")


def get_average_age():
    view.print_message("For the calculation please enter today's date [YYYY-MM-DD]: ")
    today = view.get_input("Enter here")
    view.print_general_results(hr.get_average_age(today), "The average age is: ")


def next_birthdays():
    given_date = view.get_input("Upcoming birthdays from this date [YYYY-MM-DD]")
    view.print_general_results(hr.next_birthdays(given_date), "Employee(s) birthdays in stwo weeks from given date: ")

def count_employees_with_clearance():
    given_clearance = view.get_input("Enter minimum clearance level")
    view.print_general_results(hr.count_employees_with_clearance(given_clearance), f"Employees with clearance level higher than {given_clearance}: ")


def count_employees_per_department():
    view.print_general_results(hr.count_employees_per_department(), "All departments")


def run_operation(option):
    if option == 1:
        os.system("cls||clear")
        list_employees()
    elif option == 2:
        os.system("cls||clear")
        add_employee()
    elif option == 3:
        os.system("cls||clear")
        update_employee()
    elif option == 4:
        os.system("cls||clear")
        delete_employee()
    elif option == 5:
        os.system("cls||clear")
        get_oldest_and_youngest()
    elif option == 6:
        os.system("cls||clear")
        get_average_age()
    elif option == 7:
        os.system("cls||clear")
        next_birthdays()
    elif option == 8:
        os.system("cls||clear")
        count_employees_with_clearance()
    elif option == 9:
        os.system("cls||clear")
        count_employees_per_department()
    elif option == 0:
        os.system("cls||clear")
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
