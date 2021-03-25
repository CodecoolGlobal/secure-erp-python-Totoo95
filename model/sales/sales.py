""" Sales module

Data table structure:
    - id (string)
    - transaction id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import sys, os
sys.path.append(os.getcwd())
from model import data_manager, util


def add_transaction():
    content = get_content_from_file()
    new_tansaction = []
    id = get_id()
    transaction_id = get_id()
    product = input("Product name: ")
    price = input("Price: ")
    transaction_date = input("Transaction date [YYYY-MM-DD]: ")
    
    new_tansaction.append(id)
    new_tansaction.append(transaction_id)
    new_tansaction.append(product)
    new_tansaction.append(price)
    new_tansaction.append(transaction_date)
    content.append(new_tansaction)
    write_to_file(content)


def update_transaction(id):
    content = get_content_from_file()
    for transaction in content:
        if transaction[0] == id:
            for index, data in enumerate(transaction):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    transaction[index] = new_data
    
    write_to_file(content)


def delete_transaction(id):
    content = get_content_from_file()
    for index, transaction in enumerate(content):
        if transaction[0] == id:
            content.pop(index)
    
    write_to_file(content)


def get_biggest_revenue_transaction():
    content = get_content_from_file()
    content.pop(0)
    biggest_transaction = content[0]
    for element in content:
        if float(element[3]) > float(biggest_transaction[3]):
            biggest_transaction = element
    return biggest_transaction
    

def get_biggest_revenue_product():
    content = get_content_from_file()
    content.pop(0)
    products = {}
    biggest_revenue = ("x", 0)
    for element in content:
        if element[2] in products.keys():
            products[element[2]] += float(element[3])
        else:
            products.update({element[2]: float(element[3])})
    for product, revenue in products.items():
        if revenue > biggest_revenue[1]:
            biggest_revenue = (product, revenue)
    return biggest_revenue


def get_transactions_between_dates(from_date, to_date):
    content = get_content_from_file()
    content.pop(0)
    transactions_between_dates = []
    from_date = from_date.split("-")
    to_date = to_date.split("-")
    for element in content:
        transaction_date = element[-1].split("-")
        if from_date[0] < transaction_date[0] < to_date[0]:
            transactions_between_dates.append(element)
        elif from_date[0] == transaction_date[0]:
            if from_date[1] == transaction_date[1]:
                if from_date[2] < transaction_date[2]:
                    transactions_between_dates.append(element)
                continue
            elif to_date[1] == transaction_date[1]:
                if to_date[2] < transaction_date[2]:
                    continue
            elif from_date[1] < transaction_date[1]:
                transactions_between_dates.append(element)
            continue
        elif to_date[0] == transaction_date[0]:
            if to_date[1] == transaction_date[1]:
                if to_date[2] > transaction_date[2]:
                    transactions_between_dates.append(element)
                continue
            elif to_date[1] > transaction_date[1]:
                transactions_between_dates.append(element)
            continue
    return transactions_between_dates


def count_transactions_between(from_date, to_date):
    number_of_transactions = len(get_transactions_between_dates(from_date, to_date))
    return number_of_transactions

def sum_transactions_between(from_date, to_date):
    transactions_between = get_transactions_between_dates(from_date, to_date)
    sum = 0
    for element in transactions_between:
        sum += float(element[3])
    return sum


def get_id():
    id = util.generate_id()
    return id


def write_to_file(content):
    content.pop(0)
    data_manager.write_table_to_file(DATAFILE, content)


def get_content_from_file():
    content_with_headers = data_manager.read_table_from_file(DATAFILE)
    content_with_headers.insert(0, HEADERS)

    return content_with_headers


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]
