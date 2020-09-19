from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_table(hr.list_employees1())


def add_employee():
    view.print_message("")
    
    question = ["Please enter the name for the employee: ",
                "Please enter the birthdate of the employee (yyyy-mm-dd): ",
                "Please enter the department: ",
                "Please enter the clearance from 0 to 7: "]
    answers = []
    months_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12"]
    days_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12","13",
    "14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    for item in question:
        if item != question[1]:
            user_input = view.get_input(item)
            answers.append(user_input)
            view.print_message("")
        else:
            birth_date_complete = 0
            while birth_date_complete < 1:
                user_input = view.get_input(item)
                try:
                    year, month, day = user_input.split("-")
                    if int(year) not in range(1950,2021):
                        view.print_message("Invalid year!")
                        continue
                    elif month not in months_list:
                        view.print_message("Invalid month!")
                        continue
                    elif day not in days_list:
                        view.print_message("Invalid day!")
                        continue
                    else:
                        answers.append(user_input)
                        birth_date_complete = 1
                except ValueError:
                    view.print_message("Invalid input")
    hr.add_employee1(answers[0], answers[1], answers[2], answers[3])
    view.print_message("")
    view.print_message("New employee added.")
    view.print_message("")


def update_employee():
    EMPLOYEE = 1
    BIRTHDATE = 2
    DEPARTMENT = 3
    CLEARANCE = 4
    data = hr.list_employees1()
    HEADERS = ["EMPLOYEE", "BIRTHDATE", "DEPARTMENT", "CLEARANCE"]
    counter = 0
    counter_1 = 0
    id_list = []
    for item in data:
        id_list.append(item[0])

    while counter < 1:
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the employee you want to update info: ")
        view.print_message("")
        if cust_id in id_list:
            view.print_message("Your input is valid, please see below the details:")
            view.print_message("")
            counter += 1
        else:
            view.print_message("Invalid ID")

    for inner_list in data:
        if cust_id in inner_list:
            view.print_message("ID :" + inner_list[0])
            view.print_message("EMPLOYEE: "+ inner_list[1])
            view.print_message("BIRTHDATE : "+ inner_list[2])
            view.print_message("DEPARTMENT : "+ inner_list[3])
            view.print_message("CLEARANCE : "+ inner_list[4])

    while counter_1 < 1:
        view.print_message("")
        user_input = view.get_input("Please enter the value that you want to modify \'employee\', \'birthdate\', \'department\', \'clearance\': ")
        view.print_message("")
        if user_input.upper() in HEADERS:
            view.print_message(f"{user_input.upper()} selected")
            counter_1 += 1
        else:
            view.print_message("Invalid input")
    view.print_message("")
    user_modify = view.get_input(f"Please enter the new value for {user_input.upper()}: ")
    view.print_message('')
    for inner_list in data:
        if cust_id in inner_list:
            if user_input.upper() == "EMPLOYEE":
                inner_list[EMPLOYEE] = user_modify
            elif user_input.upper() == "BIRTHDATE":                        
                inner_list[BIRTHDATE] = user_modify
            elif user_input.upper() == "DEPARTMENT":
                inner_list[DEPARTMENT] = user_modify
            elif user_input.upper() == "CLEARANCE":
                inner_list[CLEARANCE] = user_modify
    view.print_message("Update performed, please list employees to see the update.")
    hr.update_employee1(data)


def delete_employee():
    data = hr.list_employees1()
    counter = 0
    id_list = []
    for item in data:
        id_list.append(item[0])
    while counter < 1 :
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the employee that you want to delete:")
        view.print_message("")
        if cust_id in id_list:
            hr.delete_employee1(cust_id)
            view.print_message(f"Employee '{cust_id}' deleted, please list employees to see the update.")
            view.print_message("")
            counter = counter + 1
        else:
            view.print_message("Invalid ID")
            view.print_message("")


def get_oldest_and_youngest():
    view.print_message(hr.get_oldest_and_youngest1())


def get_average_age():
    view.print_error_message("Not implemented yet.")

def next_birthdays():
    answers = []
    months_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12"]
    days_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12","13",
    "14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    birth_date_complete = 0
    while birth_date_complete < 1:
        user_input = view.get_input("Please enter the starting date (yyyy-mm-dd): ")
        try:
            year, month, day = user_input.split("-")
            if int(year) not in range(1950,2021):
                view.print_message("Invalid year!")
                continue
            elif month not in months_list:
                view.print_message("Invalid month!")
                continue
            elif day not in days_list:
                view.print_message("Invalid day!")
                continue
            else:
                view.print_message("")
                if hr.next_birthdays1(user_input) == False:
                    view.print_message("There are no birthdays in the selected period.")
                else:
                    view.print_message("")
                    view.print_message(f"The following employees have birthdays in the next 2 weeks {hr.next_birthdays1(user_input)}.")
                birth_date_complete = birth_date_complete + 1
        except ValueError:
            view.print_message("Invalid input")


def count_employees_with_clearance():
    view.print_message("")
    counter = 0
    while counter < 1:
        user_input = view.get_input("Please enter the clearance value: ")
        if int(user_input) not in range(0,8):
            view.print_message("Invalid input")
        else:
            counter = counter + 1           
    if hr.count_employees_clearance1(user_input) == False:
        view.print_message(f"There are no employees with level {user_input} clearance.")
    else:
        view.print_message("")
        view.print_error_message(f"There are {hr.count_employees_clearance1(user_input)} employees with level {user_input} clearance.")    


def count_employees_per_department():
    view.print_message("")
    data = hr.count_employees_department1()
    for key,value in data.items():
       view.print_message(f"There are {value} employees in {key} department.")
    view.print_message("")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_message("")
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            view.print_message("")
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
