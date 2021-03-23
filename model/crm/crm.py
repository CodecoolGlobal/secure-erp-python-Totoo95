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

def write_to_file(content):
    content.pop(0)
    data_manager.write_table_to_file(DATAFILE, content)

def get_id():
    id = util.generate_id()
    return id

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
content = data_manager.read_table_from_file(DATAFILE)
content.insert(0, HEADERS)