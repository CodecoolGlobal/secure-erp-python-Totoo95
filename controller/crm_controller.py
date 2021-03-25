import os
from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_table(crm.get_content_from_file())

def add_customer():
    crm.add_customer()

def update_customer():
    id = view.get_input("Enter customer id")
    crm.update_customer(id)

def delete_customer():
    id = view.get_input("Enter customer id")
    crm.delete_customer(id)


def get_subscribed_emails():
    crm.get_subscribed_emails()


def run_operation(option):
    if option == 1:
        os.system("cls||clear")
        list_customers()
    elif option == 2:
        os.system("cls||clear")
        add_customer()
    elif option == 3:
        os.system("cls||clear")
        update_customer()
    elif option == 4:
        os.system("cls||clear")
        delete_customer()
    elif option == 5:
        os.system("cls||clear")
        get_subscribed_emails()
    elif option == 0:
        os.system("cls||clear")
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
