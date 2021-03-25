import os
from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller


def load_module(option):
    if option == 1:
        os.system("cls||clear")
        crm_controller.menu()
    elif option == 2:
        os.system("cls||clear")
        sales_controller.menu()
    elif option == 3:
        os.system("cls||clear")
        hr_controller.menu()
    elif option == 4:
        os.system("cls||clear")
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources",
               "Exit program"]
    
    option =view.arrow_input(f"{view.print_ascii()}\nMain menu", options)

    return option
    


def menu():
    option = None
    while option != 4:
        try:
            option = display_menu()
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    view.print_message("Good-bye!")
