import re
import json
from configure import AddressBook, Record


list_parser_word = ['add', 'change', 'phone', 'show all']


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            print('Enter a write function. Try again.')
        except ValueError:
            print('You enter a wrong value. Try again.')
        except IndexError:
            print('You enter a wrong index. Try again.')

    return inner



def parser_input(sentence):
    return re.findall(r'\w+', sentence)


@input_error
def add_contact(name, phone, birthday=None):
    Record.add_phone(phone)
    return AddressBook.add_record(name, birthday)


@input_error
def change_contact(name, new_phone):
    Record.edit_phone(new_phone)
    return print(f'You change phone number for contact {name.title()}.')


@input_error
def show_number_of_phone(name):
    return AddressBook.find(name)


def handler(parser_word):
    if parser_word == 'add':
        return add_contact
    elif parser_word == 'change':
        return change_contact
    elif parser_word == 'phone':
        return show_number_of_phone
    elif parser_word == 'show all':
        return AddressBook()
    else:
        print('Invalid command. Try again.')


def main():
    print('Hello!')
    with open('adressbook.json' 'r', newline='') as file:
        adress_book = json.load(file)
    while adress_book:
        user_input = input('Enter your command:').lower()
        if user_input == 'hello':
            print("How can I help you?")
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            with open('adressbook.json' 'a', newline='') as file:
                json.dump(AddressBook(), file)
            break
        else:
            parser_word, name, phone = parser_input(user_input)
            command = handler(list_parser_word)
            print(f'Your command {parser_word} was added successfully.')


if __name__ == '__main__':
    main()


