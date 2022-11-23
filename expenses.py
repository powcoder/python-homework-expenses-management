https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
'''
This Python exam will involve implementing a system for managing expenses.  You will
download the skeleton of the program, then implement the functions.  The design of the
program has been set up for you.

In this system, users will be able to add and deduct expenses, update expenses, sort expenses,
and export filtered expenses to a file.  The program will initially load a collection of
expenses from a .txt file and store them in a dictionary.
'''

def import_expenses(file):
    '''Reads data from a given file and stores the expenses
    in a dictionary, where the expense type is the key
    and the total expense amount for that expense is
    the value.

    The same expense type may appear multiple times in the file.
    Ignores expenses with missing or invalid amounts.
    '''

    # create empty dict
    expenses = {}

    #TODO insert your code

    return expenses

def get_expense(expenses, expense_type):
    '''Returns the value for the given expense type in the given expenses dictionary.
    Prints a friendly message and returns None if the expense type doesn't exist.
    '''

    # TODO insert your code

def add_expense(expenses, expense_type, value):
    '''Adds the given expense type and value to the given expenses dictionary.
    If the expense type already exists, adds the value to the total amount.
    Otherwise, creates a new expense type with the value.
    Prints the expense.'''

    # TODO insert your code

def deduct_expense(expenses, expense_type, value):
    '''Deducts the given value from the given expense type in the given expenses dictionary.
    Prints a friendly message if the expense type doesn't exist.
    Raises a RuntimeError if the value is greater than the existing total of the expense type.
    Prints the expense.'''

    # TODO insert your code

def update_expense(expenses, expense_type, value):
    '''Updates the given expense type with the given value in the given expenses dictionary.
    Prints a friendly message if the expense type doesn't exist.
    Prints the expense.'''

    # TODO insert your code

def sort_expenses(expenses, sorting):
    '''Converts the key:value pairs in the given expenses dictionary to
    a list of tuples and sorts based on the given sorting
    argument.

    If the sorting argument is the string ‘expense_type’,
    sorts the list of tuples based on the expense type (e.g. ‘rent’),
    otherwise, if the sorting argument is ‘amount’, sorts the list based
    on the total expense amount (e.g. 825) in descending order.
    '''

    # TODO insert your code

def export_expenses(expenses, expense_types, file):
    '''Exports the given expense types from the given expenses dictionary to the given file.

    Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
    and exports to a file.'''

    # TODO insert your code

def main():

    #import expense file and store in dictionary
    expenses = import_expenses('expenses.txt')

    #for testing purposes
    #print(expenses)

    while True:

        #print welcome and options
        print('\nWelcome to the expense management system!  What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Sort expenses')
        print('5: Export expenses')
        print('0: Exit the system')

        #get user input
        option_input = input('\n')

        #try and cast to int
        try:
            option = int(option_input)

        #catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            #check options
            if (option == 1):

                #get expense type and print expense info
                expense_type = input('Expense type? ')
                print(get_expense(expenses, expense_type))

            elif (option == 2):

                #get expense type
                expense_type = input('Expense type? ')

                #get amount to add and cast to float
                amount = float(input('Amount to add? '))

                #add expense
                add_expense(expenses, expense_type, amount)

            elif (option == 3):

                #get expense type
                expense_type = input('Expense type? ')
                #get amount to deduct and cast to float
                amount = float(input('Amount to deduct? '))

                #deduct expense
                deduct_expense(expenses, expense_type, amount)

            elif (option == 4):

                #get sort type
                sort_type = input('What type of sort? (\'expense_type\' or \'amount\')')

                #sort expenses
                print(sort_expenses(expenses, sort_type))

            elif (option == 5):

                # get filename to export to
                file_name = input('Name of file to export to?')

                # get expense types to export
                expense_types = []

                while True:
                    expense_type = input("What expense type you want to export? Input N to quit:")
                    if expense_type == "N":
                        break

                    expense_types.append(expense_type)

                # export expenses
                export_expenses(expenses, expense_types, file_name)

            elif (option == 0):

                #exit expense system
                print('Good bye!')
                break

if __name__ == '__main__':
    main()
