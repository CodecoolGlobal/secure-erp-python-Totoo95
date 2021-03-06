""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
from model import data_manager, util

def add_customer():
    content = get_content_from_file()
    new_customer = []
    id = get_id()
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
    content.append(new_customer)
    
    write_to_file(content)
    

def update_customer(id):
    content = get_content_from_file()
    for customer in content:
        if customer[0] == id:
            for index, data in enumerate(customer):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    customer[index] = new_data
    
    write_to_file(content)
    
def delete_customer(id):
    content = get_content_from_file()
    for index, customer in enumerate(content):
        if customer[0] == id:
            content.pop(index)
    
    write_to_file(content)

def get_subscribed_emails():
    content = get_content_from_file()
    subscribed_emails = []
    for customer in content:
        if customer[-1] == "1":
            subscribed_emails.append(customer[2])
    
    return subscribed_emails

def write_to_file(content):
    content.pop(0)
    data_manager.write_table_to_file(DATAFILE, content)

def get_id():
    id = util.generate_id()
    return id

def get_content_from_file():
    content_with_headers = data_manager.read_table_from_file(DATAFILE)
    content_with_headers.insert(0, HEADERS)

    return content_with_headers

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

