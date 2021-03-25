import sys, os
sys.path.append(os.getcwd())
from model.sales import sales
from view import terminal as view


def list_transactions():
    view.print_table(sales.get_content_from_file())


def add_transaction():
    sales.add_transaction()


def update_transaction():
    id = view.get_input("Enter transaction id")
    sales.update_transaction(id)


def delete_transaction():
    id = view.get_input("Enter transaction id")
    sales.delete_transaction(id)

def get_biggest_revenue_transaction():
    view.print_general_results(sales.get_biggest_revenue_transaction(), "The biggest revenue transaction")


def get_biggest_revenue_product():
    view.print_general_results(sales.get_biggest_revenue_product(), "The biggest revenue product")


def count_transactions_between():
    dates = view.get_inputs(["Give the start date", "Give the closing date"])
    view.print_general_results(sales.count_transactions_between(dates[0], dates[1]), "The number of transactions")

def sum_transactions_between():
    dates = view.get_inputs(["Give the start date", "Give the closing date"])
    view.print_general_results(sales.sum_transactions_between(dates[0], dates[1]), "The sum of the transactions between the given dates")


def run_operation(option):
    if option == 1:
        os.system("cls||clear")
        list_transactions()
    elif option == 2:
        os.system("cls||clear")
        add_transaction()
    elif option == 3:
        os.system("cls||clear")
        update_transaction()
    elif option == 4:
        os.system("cls||clear")
        delete_transaction()
    elif option == 5:
        os.system("cls||clear")
        get_biggest_revenue_transaction()
    elif option == 6:
        os.system("cls||clear")
        get_biggest_revenue_product()
    elif option == 7:
        os.system("cls||clear")
        count_transactions_between()
    elif option == 8:
        os.system("cls||clear")
        sum_transactions_between()
    elif option == 0:
        os.system("cls||clear")
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
