import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dotties_divine_doughnuts')


def log_order():
    """
    Allows user to input customer's order, uses it to calculate
    total price, and finally adds all of the order data to the
    orders worksheet.
    """
    print('You have chosen to log a customer order.\n')
    while True:
        order_size = get_order_option('size', 1)
        print(f'Great! The customer\'s doughnut will be {order_size}!\n')
        order_filling = get_order_option('filling', 3)
        print(f'The customer has chosen {order_filling} filling. No problem!')
        print('')
        order_topping = get_order_option('topping', 5)
        print(f'{order_topping} on the top, almost there!\n')
        order_num = get_order_quantity()
        print(f'Perfect, the customer wants {order_num} doughnut/s!\n')
        if confirm_order(order_size, order_filling, order_topping, order_num):
            break
        print('Okay, let\'s start again!\n')
    order_details = [order_size, order_filling, order_topping, order_num]
    total_price = calculate_total_price(order_details)
    print(f'The customer\'s total price is: £{total_price:.2f}.\n')
    order_details.append(total_price)
    update_orders_worksheet(order_details)
    service_finished('logging a customer\'s order')


def get_order_option(data, column):
    """
    Collects all available options from spreadsheet
    and collates them into a dictionary alongside
    numerical keys to make selection easier for the user.
    Returns user inputted order option.
    """
    # Collects available options from relevant column in prices worksheet.
    available_options = SHEET.worksheet('Prices').col_values(column)
    option_num = 1
    total_number_options = ()
    display_options = []
    # Creates a dictionary which assigns every option to a number as a value.
    # This makes selection easier for the user and allows the function to work
    # correctly even when the menu is adjusted.
    for option in available_options:
        if option == data:
            continue
        new_option = {option_num: option}
        display_options.append(new_option)
        total_number_options = total_number_options + tuple(str(option_num))
        int(option_num)
        option_num += 1
    print(f'The current {data} options are:')
    for option in range(len(display_options)):
        print(f'({option + 1}) - {display_options[option][option + 1]}')
    print('')
    customer_option = validate_order_option(total_number_options)
    final_selection = display_options[customer_option - 1][customer_option]
    return final_selection


def get_order_quantity():
    """
    Collects number of doughnuts desired by customer.
    Has a range of 1 - 8.
    """
    print('Finally, how many of these doughnuts would the customer like?')
    print('Please enter a number between (1) and the maximum quantity (8): \n')
    possible_quantity_values = {'1', '2', '3', '4', '5', '6', '7', '8'}
    quantity = validate_order_option(possible_quantity_values)
    return quantity


def validate_order_option(data):
    """
    Collects option from user and checks:
    - that it is an integer value
    - that it is a valid option
    returns selected option once valid.
    """
    while True:
        selection = get_user_input('Please enter the customer\'s selection:')
        try:
            int(selection)
        except ValueError as e:
            print(f'{e}, Please ensure you enter your data as a number.\n')
            continue
        int(selection)
        if selection in data:
            break
        print('Please enter a number that corresponds to the options above.\n')
    return int(selection)


def confirm_order(size, filling, topping, quantity):
    """
    Prints the complete customer order and requests confirmation.
    If correct, returns true and breaks the order loop.
    If incorrect, returns false and start the loop again.
    """
    print('Okay, here are the customer\'s complete order details:\n')
    print(f'Doughnut size: {size}')
    print(f'Doughnut filling: {filling}')
    print(f'Doughnut topping: {topping}')
    print(f'Number of Doughnuts: {quantity}\n')
    print('If this is correct: Enter (1)')
    print('If this is incorrect, and you would like to retry: Enter (2)\n')
    while True:
        complete = get_user_input('Please choose below:')
        if complete in {'1', '2'}:
            break
        print('That is an invalid option! Please choose either (1) or (2).')
    if complete == '1':
        return True
    return False


def calculate_total_price(order_details):
    """
    Uses the confirmed order details to calculate
    the total order price.
    Returns total price.
    """
    print('Calculating order price...\n')
    menu = SHEET.worksheet('Prices')
    total_price = 0.00
    for i in range(3):
        # Finds the cell which contains the selected menu item.
        item = menu.find(order_details[i])
        # Finds the item price by adding one to the item's col value.
        price = menu.cell(item.row, item.col + 1)
        item_price = float(price.value)
        # Adds each item's price to the total price.
        total_price += (item_price * 100)
    # Multiplies the total_price by the quantity of doughnuts.
    total_price *= order_details[3]
    total_price /= 100
    print('All done!')
    return total_price


def update_orders_worksheet(order):
    """
    Adds final order details to the orders worksheet.
    """
    print('Updating orders worksheet...\n')
    orders_sheet = SHEET.worksheet('Orders')
    orders_sheet.append_row(order)
    print('Updating finished.\n')


def edit_menu():
    """
    Allows user to edit the menu in a number of ways:
        1. User can add new options(sizes, fillings, toppings) to the menu.
        2. User can remove options from the menu.
        3. User can edit option prices on the menu.
    """
    print('You have chosen to edit the menu.\n')
    print('Here are the ways you can edit the menu:')
    print('(1) - Add an item to the menu')
    print('(2) - Remove an item from the menu')
    print('(3) - Edit the price of an existing item\n')
    while True:  # while loop runs until a valid input is provided.
        choice = get_user_input('What change would you like to make?')
        if choice in {'1', '2', '3'}:
            break
        print('Sorry, that is an invalid option!')
        print('Please enter either (1) or (2) or (3).\n')

    if choice == '1':
        add_menu_item()
    elif choice == '2':
        remove_menu_item()
    elif choice == '3':
        edit_item_price()


def add_menu_item():
    """
    Asks the user which menu option they would like to add to.
    Receives a desired addition and it's corresponding price,
    validates the values and appends to relevant columns on
    the prices worksheet.
    """
    print('Firstly, which order option would you like to add an item to?\n')
    category = get_menu_category()
    correct_columns_data = get_category_columns(category)
    display_columns(correct_columns_data)
    data_to_append = get_new_items(correct_columns_data)
    append_to_menu(data_to_append)
    service_finished('creating a new menu option')


def get_menu_category():
    """
    Receives the menu category to edit from the user.
    Returns the chosen category.
    """
    print('The current options are:')
    print('(1) - Doughnut sizes')
    print('(2) - Doughnut fillings')
    print('(3) - Doughnut toppings\n')
    while True:
        category = get_user_input('Which category would you like to select?')
        if category in {'1', '2', '3'}:
            break
        print('Sorry, that is an invalid option!')
        print('Please enter either (1) or (2) or (3).\n')
    return category


def get_category_columns(category):
    """
    Uses the selected menu category to collect relevant menu
    columns from the prices worksheet and returns them.
    """
    if category == '1':
        menu_options = SHEET.worksheet('Prices').col_values(1)
        menu_prices = SHEET.worksheet('Prices').col_values(2)
        menu_category = 'size'
        cols_to_update = [1, 2]
    elif category == '2':
        menu_options = SHEET.worksheet('Prices').col_values(3)
        menu_prices = SHEET.worksheet('Prices').col_values(4)
        menu_category = 'filling'
        cols_to_update = [3, 4]
    elif category == '3':
        menu_options = SHEET.worksheet('Prices').col_values(5)
        menu_prices = SHEET.worksheet('Prices').col_values(6)
        menu_category = 'topping'
        cols_to_update = [5, 6]
    del menu_options[0]
    del menu_prices[0]
    columns_data = [menu_options, menu_prices, menu_category, cols_to_update]
    return columns_data


def display_columns(columns_data):
    """
    Uses the columns list of lists to print out the
    relevant menu options in a readable format.
    """
    column_1 = columns_data[0]
    column_2 = columns_data[1]
    print(f'The current {columns_data[2]} options are:')
    for i in range(len(column_1)):
        print(f'{column_1[i]}: £{float(column_2[i]):.2f}')
    print('')


def get_new_items(data):
    """
    Receives new item information from the user
    and calls for it to be validated.
    Returns the validated data.
    """
    while True:
        print(f'Next, enter the name of the {data[2]} you would like to add.')
        print('IMPORTANT: Your data must be spelt correctly, contain only')
        print('alphabetical characters and have no spaces.')
        while True:
            new_menu_item = get_user_input('Please enter your data here:')
            if not new_menu_item.isalpha():
                print('Your data must contain only letters and no spaces.\n')
                continue
            break
        print(f'\nLastly, how much would you like your new {data[2]} to cost?')
        print('IMPORTANT: Your data must contain only numbers and be valued')
        print('in pence. Example: £0.30 would be inputted as 30.')
        while True:
            new_item_price = get_user_input('Please enter your price here:')
            try:
                int(new_item_price)
            except ValueError as e:
                print(f'{e}, Please ensure you enter your data as a number.')
                continue
            break
        if confirm_item_to_add(new_menu_item, new_item_price):
            break
        print('\nOkay, let\'s start again!')
    return [new_menu_item, float(new_item_price)/100, data[3]]


def confirm_item_to_add(item, price):
    """
    Confirms the submitted item data to be appended to menu.
    Returns True if correct.
    Returns False if incorrect.
    """
    print('\nAlright, here is your new menu option and price:')
    print(f'{item.capitalize()}: £{float(price)/100:.2f}\n')
    while True:
        confirm = get_user_input('Enter (1) if correct, otherwise enter (2):')
        if confirm in {'1', '2'}:
            break
        print('That is an invalid option! Please choose either (1) or (2).')
    if confirm == '1':
        return True
    return False


def append_to_menu(data):
    """
    Adds new item information to the relevant columns
    on the prices worksheet.
    """
    print('Okay, adding your new menu item now...\n')
    menu = SHEET.worksheet('Prices')
    item_column = SHEET.worksheet('Prices').col_values(data[2][0])
    row_to_update = len(item_column) + 1
    menu.update_cell(row_to_update, data[2][0], data[0].capitalize())
    menu.update_cell(row_to_update, data[2][1], data[1])
    print('Finished! Menu updated!\n')


def remove_menu_item():
    """
    Asks the user what item they would like to remove from menu.
    Validates input, locates item on worksheet with corresponding
    price and removes the item and price from the menu.
    """
    print('Okay, which menu category would you like to remove an item from?\n')
    category = get_menu_category()
    correct_columns_data = get_category_columns(category)
    display_columns(correct_columns_data)
    item_to_remove = get_item_to_change(correct_columns_data, 'remove')
    print('Deleting menu item now...\n')
    delete_item(item_to_remove)
    print('Menu item deleted successfully!')
    service_finished('removing a menu item')


def get_item_to_change(data, change):
    """
    Receives the item the user would like to remove/edit.
    Ensures the item exists by checking it against the available options.
    Returns the validated item.
    """
    while True:
        print(f'Next, enter the {data[2]} option you would like to {change}.')
        print('IMPORTANT: Your data must be spelt correctly and exist')
        print('in the options listed above.\n')
        while True:
            item_to_change = get_user_input('Enter the item here:\n')
            if not item_to_change.isalpha():
                print('Please make sure your data contains only letters.')
                continue
            if item_to_change.capitalize() in data[0]:
                break
            print('Please ensure your data matches one of the options above.')
        if confirm_item_to_change(item_to_change, change):
            break
        print('Let\'s start again!\n')
    return item_to_change


def confirm_item_to_change(item, change):
    """
    Confirms the submitted item data to be edited/removed the menu.
    Returns True if correct.
    Returns False if incorrect.
    """
    print(f'Is {item.capitalize()} the item you would like to {change}?')
    while True:
        confirm = get_user_input('Enter (1) if correct, otherwise enter (2):')
        if confirm in {'1', '2'}:
            break
        print('That is an invalid option! Please choose either (1) or (2).')
    if confirm == '1':
        return True
    return False


def delete_item(item):
    """
    Uses passed in item to locate cells to be deleted.
    To avoid leaving gaps in the worksheet columns,
    swaps the values of the cells to be deleted with
    the last cells of the columns before deleting.
    """
    menu = SHEET.worksheet('Prices')
    # locates the cell to be deleted.
    item_cell = menu.find(item.capitalize())
    # uses cell data to collect all column values.
    item_column = menu.col_values(item_cell.col)
    # finds the last item in the column using len()
    last_item_row = len(item_column)
    # stores last cell data for both columns to be edited.
    last_item_cell = menu.cell(last_item_row, item_cell.col)
    last_price_cell = menu.cell(last_item_row, item_cell.col + 1)
    # replaces cells to be deleted with values of bottom cells.
    menu.update_cell(item_cell.row, item_cell.col, last_item_cell.value)
    menu.update_cell(item_cell.row, item_cell.col + 1, last_price_cell.value)
    # deletes the now repeat cells at the bottom of the columns
    menu.update_cell(last_item_cell.row, last_item_cell.col, '')
    menu.update_cell(last_price_cell.row, last_price_cell.col, '')


def edit_item_price():
    """
    Asks user for item to be edited and requests new price.
    Locates item on prices worksheet and edits the price.
    """
    print('Firstly, which category is the item you would like to edit in?\n')
    category = get_menu_category()
    correct_columns_data = get_category_columns(category)
    display_columns(correct_columns_data)
    item_to_edit = get_item_to_change(correct_columns_data, 'edit')
    new_price = get_new_price(item_to_edit)
    print(new_price)


def get_new_price(item):
    """
    Uses selected item to find current price and print both to user.
    Asks the user what tehy would like the new price to be and returns it.
    """
    menu = SHEET.worksheet('Prices')
    menu_item = menu.find(item.capitalize())
    price = menu.cell(menu_item.row, menu_item.col + 1)
    print(f'{menu_item.value} currently costs £{float(price.value):.2f}.\n')
    while True:
        print(f'What would you like the new cost of {item} to be?')
        print('IMPORTANT: Your data must contain only numbers and be valued')
        print('in pence. Example: £0.30 would be inputted as 30.')
        while True:
            new_price = get_user_input('Enter the new price here:')
            try:
                int(new_price)
            except ValueError as e:
                print(f'{e}, Please ensure you enter your data as a number.')
                continue
            break
        if confirm_item_price(item, float(new_price)):
            break
        print('Please try again.')
    return float(new_price)/100


def confirm_item_price(item, price):
    """
    Confirms the new item price.
    Returns True if correct.
    Returns False if incorrect.
    """
    print(f'Okay, would you like {item} to cost £{price/100:.2f}?\n')
    while True:
        confirm = get_user_input('Enter (1) if correct, otherwise enter (2):')
        if confirm in {'1', '2'}:
            break
        print('That is an invalid option! Please choose either (1) or (2).')
    if confirm == '1':
        return True
    return False


def view_analytics():
    """
    Calculates a number of helpful analytics from recent orders
    and displays them to the user.
    """


def service_finished(service_string):
    """
    This function is called when the user finishes using a service.
    It allows them to return to the menu to complete a new task or
    exit the application.
    """
    print(f'Great! You have now finished {service_string}!\n')
    print('What would you like to do next:')
    print('(1) - Return to main menu.')
    print('(2) - Exit the program.\n')
    while True:
        choice = get_user_input('Please enter your choice below:')
        if choice in {'1', '2'}:
            break
        print('Sorry, that is an invalid option!')
        print('Please enter either (1) or (2).\n')
    if choice == '1':
        print('Okay, returning to main menu!\n')
        main()
    elif choice == '2':
        print('See you later! Exiting application...\n')
        sys.exit(0)


def get_user_input(message):
    """
    This function is called every time a user input is required,
    it standardizes the UX by keeping consistent design features
    all in one place.
    Also checks if the user input is either 'exit' or 'main'
    and responds accordingly.
    Returns user input.
    """
    user_input = input(f'{message}\n').strip().lower()
    if user_input == 'exit':
        print('See you later! Exiting application...\n')
        sys.exit(0)
    if user_input == 'main':
        print('Okay, returning to main menu!\n')
        main()
    return user_input


def main():
    """
    Welcomes the user and explains functionality of
    the choices provided. The user can choose one of three
    options:
        1. Log a current customer's order and calculate their total price.
        2. Edit the menu (Add/Remove options, Change prices).
        3. View some analytics about recent orders.
    """
    print('Here are the services currently provided:')
    print('(1) - Log Current Customer Order')
    print('(2) - Edit Menu')
    print('(3) - View Analytics\n')

    while True:  # while loop runs until a valid input is provided.
        choice = get_user_input('Which service would you like to access?')
        if choice in {'1', '2', '3'}:
            break
        print('Sorry, that is an invalid option!')
        print('Please enter either (1) or (2) or (3).\n')

    if choice == '1':
        log_order()
    elif choice == '2':
        edit_menu()
    elif choice == '3':
        view_analytics()


if __name__ == "__main__":
    print('Welcome to \'Dottie\'s Divine Doughnuts\' services application!\n')
    print('Enter \'exit\' to exit the program at any time.')
    print('Enter \'main\' to return to the main menu at any time.\n')
    main()
