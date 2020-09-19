from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_message("")
    crm_info = crm.get_CRM_info()
    view.print_table(crm_info)


def add_customer():
    view.print_message("")
    questions = ["Please enter the name for the new customer:",
                 "Please enter the email address for the new customer:",
                 "Please enter \"yes\" or \"no\" if the new customer is subscribed to our news letter:"]
    answers = []
    for item in questions:
        if item != questions[-1]:
            user_input = view.get_input(item)
            answers.append(user_input)
            view.print_message("")
        else:
            counter = 0
            while counter < 1 :
                user_input = view.get_input(item)
                if user_input == "yes":
                    answers.append("1")
                    counter = counter + 1
                elif user_input == "no":
                    answers.append("0")
                    counter = counter + 1
                else:
                    view.print_message("Invalid input")
                    continue
    crm.create_new_customer(answers[0],answers[1],answers[2])
    view.print_message("")
    view.print_message("New customer added, please list customers to see the update.")
    view.print_message("")


def update_customer():
    NAME = 1
    EMAIL = 2
    SUBSCRIBED = 3
    data = crm.get_CRM_info()
    HEADERS = ["NAME", "EMAIL", "SUBSCRIBED"]
    counter = 0
    counter_1 = 0
    id_list = []
    for item in data:
        id_list.append(item[0])

    while counter < 1 :
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the client for which you want to perform updates:")
        view.print_message("")
        if cust_id in id_list:
            view.print_message("Your input is valid, please see below the details:")
            view.print_message("")
            counter = counter + 1
        else:
            view.print_message("Invalid ID")
            
    for inner_list in data:
        if cust_id in inner_list :
            view.print_message("ID : "+ inner_list[0])
            view.print_message("NAME : "+ inner_list[1])
            view.print_message("EMAIL : "+ inner_list[2])
            view.print_message("SUBSCRIBED : "+ inner_list[3])

    while counter_1 < 1:
        view.print_message("")
        user_input = view.get_input("Please enter the value that you want to modify \"name\", \"email\" or \"subscribed\":")
        view.print_message("")
        if user_input.upper() in HEADERS:
            view.print_message(f"{user_input.upper()} selected")
            counter_1 = counter_1 + 1
        else:
            view.print_message("Invalid input")
    view.print_message("")
    user_modify = view.get_input(f"Please enter the new value for {user_input.upper()}:")
    view.print_message("")
    for inner_list1 in data:
        if cust_id in inner_list1:
            if user_input.upper() == "NAME":
                inner_list1[NAME] = user_modify
            elif user_input.upper() == "EMAIL":
                inner_list1[EMAIL] = user_modify
            elif user_input.upper() == "SUBSCRIBED":
                inner_list1[SUBSCRIBED] = user_modify 
    view.print_message("Update performed, please list customers to see the update.")
    crm.update_customer_info(data)


def delete_customer():
    data = crm.get_CRM_info()
    counter = 0
    id_list = []
    for item in data:
        id_list.append(item[0])
    while counter < 1 :
        view.print_message("")
        cust_id = view.get_input("Please enter the id of the client that you want to delete:")
        view.print_message("")
        if cust_id in id_list:
            crm.delete_customer(cust_id)
            view.print_message(f"Customer '{cust_id}' deleted, please list customers to see the update.")
            view.print_message("")
            counter = counter + 1
        else:
            view.print_message("Invalid ID")
            view.print_message("")



def get_subscribed_emails():
    view.print_message("")
    view.print_message(f"The e-mails are {crm.get_subscribed_customers_email()}")
    view.print_message("")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_message("")
    view.print_menu("Customer Relationship Management", options)


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
