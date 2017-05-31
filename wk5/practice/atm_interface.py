# atm_interface
import os
from account import Account

act = Account
YESCHOICES = ('Y', 'Yes', 'yes', 'YEs' )

def create_account() -> act:
    """
    Returns the type from the class Account
    """
    welcome_display()

    first_name = input('Please enter your first name:>> ')
    surname = input('Please enter your last name:>> ')
    accountype = {1: 'checking', 2: 'savings', 3: 'checking&savings'}
    print(accountype)
    acc_choice = input('Enter type of account desired:')
    if acc_choice == 1:
        accountype[1]
    elif acc_choice == 2:
        accountype[2]
    elif acc_choice == 3:
        accountype[3]

    account = Account(first_name=first_name, surname=surname, accountype=accountype)    # account is local var; it calls Class, requires kwargs
    pin = input('Create a 4-digit PIN:>> ')

    print(account._account_number)
    print(account.fullname)
    print(account.accountype)
    print('Write down your PIN. Store PIN in a safe place:', pin)
    print(account)


def menu():
    """
    Provide menu options: balance, withdrawal; deposit; check YTD interest

    """

    account = create_account()

    options = {1: 'balance', 2: 'withdrawal', 3: 'deposit', 4: 'interest_YTD', 5: exit}    # purpose anymore?
    print(options)

    userinp = int(input('Enter a menu number to performs a transaction>> '))    # TODO: Build try, except if not a number.

    wid_amt = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100, 6: 200}    # TODO: Create 'other amount' option for key in value.
    print(wid_amt)

    if userinp == 1:
        bal = account.get_funds()
        print(int(bal))
    elif userinp == 2:
        wid_opt = int(input("Enter number option for withdrawal amount>> "))
        if wid_opt == 1:
            amount = wid_amt[1]    # May also use; wid_amt[1]--this will show a traceback error.
            account.withdraw(amount)
        elif wid_opt == 2:
            amount = wid_amt[2]
            account.withdraw(amount)
        elif wid_opt == 3:
            amount = wid_amt[3]
            account.withdraw(amount)
        elif wid_opt == 4:
            amount = wid_amt[4]
            account.withdraw(amount)
        elif wid_opt == 5:
            amount = wid_amt[5]
            account.withdraw(amount)
        elif wid_opt == 6:
            amount = wid_amt[6]
            account.withdraw(amount)
    elif userinp == 3:
        dep_amt = int(input("Enter exact dollar amount for deposit>>  "))
        amount = dep_amt
        account.deposit(amount)
    elif userinp == 4:
        interest = account.calc_interest()
        print(interest, 'YTD')
    elif userinp == 5:
        exit()

    adl_trans =input('Do you want another transaction? Y/N>> ')
    if adl_trans in YESCHOICES:
        options
    else:
        exit()

    # print(options)
    # cmd = None
    # while cmd != 'exit':
    #     choice = input('1 (account balance), 2 (withdrawal), 3 (deposit), 4 (Interest YTD)')
    #     print(options[choice]())

def welcome_display():
    """
    Welcome + instructions 
    Return card to user
    """
    message = f'''  
                Welcome to FARE FINTA Credit Union. If you do not have an account, 
                please create one.  Otherwise, insert card and enter your PIN.
                '''
    print(message)

create_account()    # This starts the program by directly jumping to the create_account

# def preexisting_account():









