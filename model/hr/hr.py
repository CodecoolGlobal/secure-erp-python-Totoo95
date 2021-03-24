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


def add_employee():
    content = get_content_from_file()
    new_employee = []
    id = get_id()
    name = input("Enter name: ")
    birthdate = input("Enter birthate [YYYY-MM-DD]: ")
    department = input("Enter department: ")
    clearence = input("Clearence level: ")
    
    new_employee.append(id)
    new_employee.append(name)
    new_employee.append(birthdate)
    new_employee.append(department)
    new_employee.append(clearence)
    content.append(new_employee)
    write_to_file(content)


def update_emmployee(id):
    content = get_content_from_file()
    for employee in content:
        if employee[0] == id:
            for index, data in enumerate(employee):
                if data != id:
                    print("Old data: " + data)
                    new_data = input("For no change press ENTER, else: New data: ")
                    if new_data == "":
                        continue
                    employee[index] = new_data
    
    write_to_file(content)


def delete_employee(id):
    content = get_content_from_file()
    for index, employee in enumerate(content):
        if employee[0] == id:
            content.pop(index)
    write_to_file(content)


def get_oldest_and_youngest():
    content = get_content_from_file()
    content.pop(0)
    birthdays = {}
    for customers in content:
        birthdays.update({customers[0]: customers[2]})
    year, month, day = 10000, 13, 32
    for key, value in birthdays.items():
        if int(value.split("-")[0]) < year:
            year = int(value.split("-")[0])
            oldest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) < month:
            month = int(value.split("-")[1])
            oldest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) == month and int(value.split("-")[2]) < day:
            day = int(value.split("-")[2])
            oldest_id = key
    
    year, month, day = 0, 0, 0
    for key, value in birthdays.items():
        if int(value.split("-")[0]) > year:
            year = int(value.split("-")[0])
            youngest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) > month:
            month = int(value.split("-")[1])
            youngest_id = key
        elif int(value.split("-")[0]) == year and int(value.split("-")[1]) == month and int(value.split("-")[2]) > day:
            day = int(value.split("-")[2])
            youngest_id = key
    
    for employee in content:
        if employee[0] == oldest_id:
            oldest_id += " " + employee[1] + " " + employee[2]
    
    for employee in content:
        if employee[0] == youngest_id:
            youngest_id += " " + employee[1] + " " + employee[2]
    
    return (oldest_id, youngest_id)


def get_average_age(today):
    content = get_content_from_file()
    content.pop(0)
    birthdates = []
    today = today.split("-")
    for employee in content:
        birthdates.append(employee[2])
    sum_age = 0
    for birth in birthdates:
        birth = birth.split("-")
        age = int(today[0]) - int(birth[0])
        if int(today[1]) == int(birth[1]) and int(today[2]) == int(birth[2]):
            sum_age += age
            continue
        elif int(today[1]) <= int(birth[1]):
            if int(today[2]) < int(birth[2]) and int(today[1]) == int(birth[1]):
                age -= 1
                sum_age += age
                continue
            age -= 1
        sum_age += age
    
    avg_age = float(sum_age/len(birthdates))
    
    return avg_age


def next_birthdays(given_date):
    content = get_content_from_file()
    content.pop(0)
    birthdates = {}
    following_birthdays_id = []
    following_birthdays = []
    month_and_days = {
        "01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31
    }
    for employee in content:
        birthdates.update({employee[0]: employee[2]})
    days_given = 0
    days_employee = 0
    given_date = given_date.split("-")
    for key, value in month_and_days.items():
        if key != given_date[1]:
            days_given += value

        elif key == given_date[1]:
            days_given += int(given_date[2])
            break

    for id, day in birthdates.items():
        day = day.split("-")
        days_employee = 0
        for key, value in month_and_days.items():
            if key != day[1]:
                days_employee += value

            elif key == day[1]:
                days_employee += int(day[2])
                break
        
        if days_given > 351:
            days_employee += 365
        days = days_employee - days_given
        
        if days in range(15):
            following_birthdays_id.append(id)
    
    for employee in content:
        if employee[0] in following_birthdays_id:
            person = f"{employee[0]} {employee[1]} {employee[2]}"
            following_birthdays.append(person)
    
    return following_birthdays


def get_employees_by_given_data(index):
    content = get_content_from_file()
    content.pop(0)
    all_data = {}
    for employee in content:
        if employee[index] in all_data.keys():
            all_data[employee[index]] += 1
        else:
            all_data.update({employee[index]: 1})
    
    return all_data


def count_employees_with_clearance(given_clearance):
    all_clearances = get_employees_by_given_data(-1)
    needed_clearances = {}
    for clearance, level in all_clearances.items():
        if clearance >= given_clearance:
            needed_clearances.update({f"level {clearance}": level})

    return needed_clearances

def count_employees_per_department():
    all_departments = get_employees_by_given_data(3)
    return all_departments

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

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
