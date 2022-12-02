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
    order_size = get_order_option('size')
    order_filling = get_order_option('filling')
    order_topping = get_order_option('topping')


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
    display_options = []
    # Creates a dictionary which assigns every option to a number as a value.
    # This makes selection easier for the user and allows the function to work
    # correctly even when the menu is adjusted.
    for option in available_options:
        if option == data:
            continue
        new_option = {option_num: option}
        display_options.append(new_option)
        option_num += 1
    print(f'The current {data} options are:')
    for option in range(len(display_options)):
        print(f'({option + 1}) - {display_options[option][option + 1]}')
    print('')
    customer_option = input('Please enter the customer\'s selection below:')
    print(customer_option)


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
        choice = input('Which service(1, 2, 3) would you like to access?\n')
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
