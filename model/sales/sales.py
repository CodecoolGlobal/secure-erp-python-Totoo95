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
