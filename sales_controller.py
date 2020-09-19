from model.sales import sales
from view import terminal as view


def list_transactions():
    view.print_message("")
    view.print_table(sales.list_transactions1())


def add_transaction():
    view.print_message("")
    
    question = ["Please enter the name for the customer: ",
                "Please enter the product sold: ",
                "Please enter the price: ",
                "Please enter the date of the transaction(yyyy-mm-dd): "]
    answers = []
    months_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12"]
    days_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12","13",
    "14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    for item in question:
        if item != question[-1]:
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
    sales.add_transaction1(answers[0], answers[1], answers[2], answers[3])
    view.print_message("")
    view.print_message("New transaction added.")
    view.print_message("")


def update_transaction():
    CUSTOMER = 1
    PRODUCT = 2
    PRICE = 3
    DATE = 4
    data = sales.list_transactions1()
    HEADERS = ["CUSTOMER", "PRODUCT", "PRICE", "DATE"]
    counter = 0
    counter_1 = 0
    id_list = []
    for item in data:
        id_list.append(item[0])

    while counter < 1:
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the costumer you want to update info: ")
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
            view.print_message("CUSTOMER: "+ inner_list[1])
            view.print_message("PRODUCT : "+ inner_list[2])
            view.print_message("PRICE : "+ inner_list[3])
            view.print_message("DATE : "+ inner_list[4])

    while counter_1 < 1:
        view.print_message("")
        user_input = view.get_input("Please enter the value that you want to modify \'customer\', \'product\', \'price\', \'date\': ")
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
            if user_input.upper() == "CUSTOMER":
                inner_list[CUSTOMER] = user_modify
            elif user_input.upper() == "PRODUCT":
                inner_list[PRODUCT] = user_modify
            elif user_input.upper() == "PRICE":
                inner_list[PRICE] = user_modify
            elif user_input.upper() == "DATE":
                inner_list[DATE] = user_modify
    view.print_message("Update performed, please list customers to see the update.")
    sales.update_transaction1(data)


def delete_transaction():
    data = sales.list_transactions1()
    counter = 0
    id_list = []
    for item in data:
        id_list.append(item[0])
    while counter < 1 :
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the client that you want to delete:")
        view.print_message("")
        if cust_id in id_list:
            sales.delete_transaction1(cust_id)
            view.print_message(f"Customer '{cust_id}' deleted, please list customers to see the update.")
            view.print_message("")
            counter = counter + 1
        else:
            view.print_message("Invalid ID")
            view.print_message("")


def get_biggest_revenue_transaction():
    view.print_message("")
    view.print_message(sales.get_biggest_revenue_transaction1())
    view.print_message("")


def get_biggest_revenue_product():
    view.print_message("")
    view.print_message(sales.get_biggest_revenue_product1())
    view.print_message("")


def count_transactions_between():
    months_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12"]
    days_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12","13",
    "14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    answers = []
    birth_date_complete = 0
    while birth_date_complete < 2:
        user_input = view.get_input("Please enter the date of the transaction(yyyy-mm-dd): ")
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
                birth_date_complete = birth_date_complete + 1
        except ValueError:
            view.print_message("Invalid input")   
    view.print_message("")
    view.print_message(f"There are {sales.count_transactions_between1(answers[0],answers[1])} transactions between {answers[0]} and {answers[1]}.")


def sum_transactions_between():
    months_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12"]
    days_list = ["01","02","03","04","05","06",'07','08','09',"10","11","12","13",
    "14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    answers = []
    birth_date_complete = 0
    while birth_date_complete < 2:
        user_input = view.get_input("Please enter the date of the transaction(yyyy-mm-dd): ")
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
                birth_date_complete = birth_date_complete + 1
        except ValueError:
            view.print_message("Invalid input")   
    view.print_message("")
    view.print_message(f"The sum is {sales.sum_transactions_between1(answers[0],answers[1])} dollars for the transactions between {answers[0]} and {answers[1]}.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_message("")
    view.print_menu("Sales", options)


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
