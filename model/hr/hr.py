""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
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

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
content = data_manager.read_table_from_file(DATAFILE)
content.insert(0, HEADERS)