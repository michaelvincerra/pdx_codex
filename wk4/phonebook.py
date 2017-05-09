


phonebook = {'Kieran': {'name': 'Kieran', 'number': 8456331959, 'nick_name': 'Bomber'},    # dict in dict: Access by keys!
            'Michael': {'name': 'Michael', 'number': 8454185633, 'nick_name': 'Lino'},
            'Elizabeth': {'name': 'Elizabeth', 'number': 5031234567, 'nick_name': 'Betsy'}}


print('Welcome to your phone book of contacts.')
print('Here\'s a view of your current contacts by name.')
print('Press Enter to continue, or type "exit" to quit')
print(phonebook.keys())


def lister():
    option = input('Show contacts>> Y/N  ').casefold()
    if option in ('Y', 'y'):
        print(phonebook.items())
    elif option in ('N', 'n'):
        main()

"""
    if query_name in phonebook.keys():
        print(phonebook[query_name])    # option is passed here as searched on thing
    else:
        print('That name is not available.')
"""

def new_contact():

    # print('Create new contact.')
    # new_name = input('Enter name>> ')   # Add new
    # new_num = input('Enter number>> ')
    # new_nick = input('Enter nickname>> ')

    name = input('Enter name>>> ')
    number = input('Enter number>> ')
    nick_name = input('Enter nickame>> ')

    contact = {'name': name, 'number': number, 'nick_name': nick_name}

    #phonebook[name] = contact   # key assignment; mutates dict

    update_data = {name: contact}   # contact, above, creates a new dictionary item; that is consumed here in 'update-data' as a dictionary (within a dictionary)

    phonebook.update(update_data)   # dict.update(new_var).... allows the original dictionary to be updated with a new dict within the dict.

    print(phonebook.keys())


def setter():
    query_name = input('Search by name>> ')
    try:
        print(phonebook[query_name])  # option 'query_name' is passed here as searched for name
    except KeyError:
        print('That name is not available. Entries are case sensitive')

    new_cont = input('Do you want to create a new Contact? Y/N>>'.casefold())
    if new_cont in ('Y', 'y'):
        new_contact()

        option_editor = int(input('Modify: 1(name), 2(number), 3(nick_name)>> '))    # TODO: Finish SECTION Below

        if option_editor == 1:
            new_name = input('Overwrite name>> ')
            # phonebook.update(editor)
            # phonebook[query_name]['name'] = new_name  # mutates. updates dict. similar to item assignment

            phonebook[query_name] = dict([phonebook(new_name)])

            print('Success!')
            print(phonebook[query_name])

        elif option_editor == 2:
            new_num = input('Overwrite number>> ')
            phonebook[query_name]['number'] = new_num
            print('Success!')
            print(phonebook[query_name])

        elif option_editor == 3:
            new_nick = input('Overwrite nickname>> ')
            phonebook[query_name]['nick_name'] = new_nick
            print('Success!')
            print(phonebook[query_name])

        else:
            main()


def getter():
    query_cont = input('Enter name:>>  ')

    try:
        contact = phonebook[query_cont]

    except KeyError:
        print(f'{query_cont} not found.')
        return getter()

    for key in contact:
        print(key, contact[key], sep=' ---> ', end='\n-------\n')


def main():
    options = {'1': lister, '2': setter, '3': getter, '4': new_contact, '5': exit}
    cmd = None
    while cmd != 'exit':
        choice = input('To change contacts, enter: 1(list), 2(modify), 3(get), or 4(new contact), 5(exit)')
        options[choice]()

main()





    #         if cmd == 'list':
    #             for name in phonebook:
    #                 print(name)
    #
    #         elif cmd == 'add':
    #             print('Name?')
    #             name = input()
    #             print ('Phone Number?')
    #             number = input()
    #
    #         elif cmd == 'get':
    #             print('Name?')
    #             name = input()
    #             number = phonebook.get(name, 'No Entry')
    #             print(name + '---' + number)
    #         else:
    #             print('Unknown command:' + cmd)
    #
    #
    # main()


    #
    #
    # usr_inp1 = input('')
    # usr_inp2
    # usr_inp3

    # def phone_book():
