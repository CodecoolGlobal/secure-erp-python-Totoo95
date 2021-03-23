from model.util import generate_id


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    pass


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    number_of_columns = len(table[0])
    longest_datas = []
    for i in range(number_of_columns):
        maximum_len = 0
        for customers in table:
            if len(str(customers[i])) > len(str(maximum_len)):
                maximum_len = customers[i]
        longest_datas.append(maximum_len)
    first_line = "/"
    for count in range(len(longest_datas)):
        first_line += "-" + "-" *len(str(longest_datas[count])) + "-"
    first_line += "-\\"

    print(first_line)
    for index in range(len(table)):
        header_line = ""
        for index, title in enumerate(table[index]):
            needed_spaces = len(str(longest_datas[index])) - len(str(title)) + 2
            header_line += "|" + (needed_spaces//2)*" " + title + " " *(needed_spaces//2)
        
        print(header_line + "|")
        first_line = first_line.replace("\\", "|").replace("/", "|")
        print(first_line)
    

        



def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    pass


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    new_customer = []
    id = generate_id()
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
    
    return new_customer



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
