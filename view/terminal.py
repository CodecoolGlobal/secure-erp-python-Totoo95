import os


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
    print(f"{title}: ")
    counter = 1
    exit = list_options[0]
    list_options.pop(0)
    for option in list_options:
        print(f"[{counter}] {option}")
        counter += 1
    counter = 0
    print(f"[{counter}] {exit}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) is int:
        print(f"{label}: {result}")
    elif type(result) is float:
        print(label + ": "  + "%.2f" %result)
    elif type(result) is list or type(result) is tuple:
        print(f"{label}: ")
        print_text = ""
        for data in result:
            print_text += str(data) + "; "
        print(print_text)
    elif type(result) is dict:
        print(f"{label}: ")
        print_text = ""
        for key, value in result.items():
            print_text += str(key) + ": " + str(value) + "; "
        print(print_text)
    input("\nPress enter to return to menu!")
    os.system("cls||clear")


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
    first_line = "+"
    for count in range(len(longest_datas)):
        first_line += "-"*(len(str(longest_datas[count]))+4)
    first_line += (number_of_columns-1)*"-" + "+"
    print(first_line)

    for index in range(len(table)):
        header_line = ""
        for key, title in enumerate(table[index]):
            aligned_title = title.center(len(longest_datas[key])+4)
            header_line += "|" + aligned_title
        
        print(header_line + "|")
        first_line = first_line.replace("+", "|")
        if index == len(table)-1:
            first_line = first_line.replace(first_line[0], "+")
        print(first_line)
    input("\nPress enter to return to menu!")
    os.system("cls||clear")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    
    data = input(f"{label}: ")

    return data


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    datas = []
    for label in labels:
        datas.append(input(f"{label}: "))
    
    return datas


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
