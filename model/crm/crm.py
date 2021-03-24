""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
import sys, os
sys.path.append(os.getcwd())
from model import data_manager, util

def add_customer():
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
    write_to_file()
    

def update_customer():
    for customer in content:
        if customer[0] == id:
            for index, data in enumerate(customer):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    customer[index] = new_data
    
    write_to_file()
    
def delete_customer():
    for index, customer in enumerate(content):
        if customer[0] == id:
            content.pop(index)
    
    write_to_file(content)

def get_subscribed_emails():
    subscribed_emails = []
    for customer in content:
        if customer[-1] == "1":
            subscribed_emails.append(customer[2])
    
    for email in subscribed_emails:
        print(email)

def write_to_file():
    data_manager.write_table_to_file(DATAFILE, content)

def get_id():
    id = util.generate_id()
    return id

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
content = data_manager.read_table_from_file(DATAFILE)
content_with_headers = content.copy()
content_with_headers.insert(0, HEADERS)