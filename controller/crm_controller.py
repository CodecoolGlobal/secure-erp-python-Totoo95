import sys, os
sys.path.append(os.getcwd())
from model.crm import crm
from view import terminal as view


def list_customers():
    #view.print_error_message("Not implemented yet.")

    view.print_table(crm.content)

def add_customer():
    #crm.content.append(view.get_inputs([]))
    new_customer = []
    id = crm.get_id()
    name = input("Enter name: ")
    e_mail = input("Enter e-mail address: ")
    subscribed = input("Subscription [Y/N]: ").upper()
    if subscribed == "Y":
        subscribed = str(1)
    elif subscribed == "N":
        subscribed = str(0)
    
    new_customer.append(id)
    new_customer.append(name)
    new_customer.append(e_mail)
    new_customer.append(subscribed)
    crm.content.append(new_customer)
    crm.write_to_file(crm.content)


def update_customer():
    id = input("Enter customer id: ")
    for customer in crm.content:
        if customer[0] == id:
            for index, data in enumerate(customer):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    customer[index] = new_data
    
    crm.write_to_file(crm.content)



def delete_customer():
    id = input("Enter customer id: ")
    for index, customer in enumerate(crm.content):
        if customer[0] == id:
            crm.content.pop(index)
    crm.write_to_file(crm.content)


def get_subscribed_emails():
    subscribed_emails = []
    for customer in crm.content:
        if customer[-1] == "1":
            subscribed_emails.append(customer[2])
    
    for email in subscribed_emails:
        print(email)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
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
