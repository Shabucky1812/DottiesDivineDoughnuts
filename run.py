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
    Allows user to input customer's order and adds it to
    orders worksheet.
    Also calculates customer's total price.
    """
    print('You have chosen to log a customer order.\n')
    while True:
        order_size = get_order_option('size')
        print(f'Great! The customer\'s doughnut will be {order_size}!\n')
        order_filling = get_order_option('filling')
        print(f'The customer has chosen {order_filling}. No problem!\n')
        order_topping = get_order_option('topping')
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


def get_order_option(data):
    """
    Collects all available options from spreadsheet
    and collates them into a dictionary alongside
    numerical keys to make selection easier for the user.
    Returns user inputted order option.
    """
    # Collects available options from relevant column in prices worksheet.
    if data == 'size':
        available_options = SHEET.worksheet('Prices').col_values(1)
    elif data == 'filling':
        available_options = SHEET.worksheet('Prices').col_values(3)
    elif data == 'topping':
        available_options = SHEET.worksheet('Prices').col_values(5)
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
    customer_option = validate_option(total_number_options)
    final_selection = display_options[customer_option - 1][customer_option]
    return final_selection


def get_order_quantity():
    """
    Collects number of doughnuts desired by customer.
    Has a range of 1 - 8.
    """
    print('Finally, how many of these doughnuts would the customer like?')
    print('Please enter a number between (1) and the maximum quantity (8): \n')
    possible_quantity_values = ('1', '2', '3', '4', '5', '6', '7', '8')
    quantity = validate_option(possible_quantity_values)
    return quantity


def validate_option(data):
    """
    Collects option from use and checks:
    - that it is an integer value
    - that it is a valid option
    returns selected option once valid.
    """
    while True:
        selection = input('Please enter the customer\'s selection:\n').strip()
        try:
            int(selection)
        except ValueError as error:
            print(f'{error}, Please ensure you enter data as a number:\n')
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
        complete = input('Please choose below:\n').strip()
        if complete == '1' or complete == '2':
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


def view_analytics():
    """
    Calculates a number of helpful analytics from recent orders
    and displays them to the user.
    """


def main():
    """
    Welcomes the user and explains functionality of
    the choices provided. The user can choose one of three
    options:
        1. Log a current customer's order and calculate their total price.
        2. Edit the menu (Add/Remove options, Change prices).
        3. View some analytics about recent orders.
    """
    print('Welcome to \'Dottie\'s Divine Doughnuts\' services application!\n')
    print('Here are the services currently provided:')
    print('(1) - Log Current Customer Order')
    print('(2) - Edit Menu')
    print('(3) - View Analytics\n')

    while True:  # while loop runs until a valid input is provided.
        choice = input('Which service would you like to access?\n').strip()
        if choice in ('1', '2', '3'):
            break

        print('Sorry, that is an invalid option!')
        print('Please enter either \'1\' or \'2\' or \'3\'.\n')

    if choice == '1':
        log_order()
    elif choice == '2':
        edit_menu()
    elif choice == '3':
        view_analytics()


main()
