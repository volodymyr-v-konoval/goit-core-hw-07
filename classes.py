from collections import UserDict

class Field:
    '''
    It's the parrent class for fields with strings.
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    '''
    It's a special class for a person's name in the phonebook.
    '''
    def __init__(self, value):
        self.value = value
        if not self.value:
            print('Enter a name, please!')

class Phone(Field):
    '''
    It's a special class, with validation,
    for phone numbers in the phonebook.
    '''
    def __init__(self, value):
        if len(value) == 10 and str(value).isdigit:
            self.value = value
        else:
            raise ValueError

class Record:
    '''
    It's a class to prepare and edit data in the phonebook.
    '''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        '''
        The function adds the Phone object to the phonebook.
        '''
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        '''
        The function removes the phone object, with value
        equal to the phone argument, from the phonebook.
        '''
        for phone_object in self.phones:
            if phone_object.value == phone:
                self.phones.remove(phone_object)

    def edit_phone(self, old: str, new: str) -> None:
        '''
        The function replaces one phone object in the phonebook,
        to another, using other functions of the class.
        '''
        self.remove_phone(old)
        self.add_phone(new)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    '''
    It's a special custom dictionary to use it as a phonebook.
    '''

    def add_record(self, data: Record) -> None:
        '''
        Adds a apecial Record object as a note 
        in the phonebook dictionary.
        '''
        self.data[data.name.value] = data

    def find(self, name: str) -> Record | None:
        '''
        If founds key, equal to the name argunent, 
        returns the Record object, which is 
        the value in the phonebook dictionary. 
        Otherwise returns None.
        '''
        if name in self.data.keys():
            return self[name]
        return None
    
    def delete(self, name: str) -> None:
        '''
        The function removes the note from the phonebook
        with the key equal to the name argument.
        '''
        if name in self.data.keys:
            self.data.pop(name)

    def __str__(self):
        dict_to_string = ''
        for rec in self.values():
            dict_to_string += (f"Contact name: {rec.name.value}, phones: {'; '.join(p.value for p in rec.phones)}\n")       
        return dict_to_string.strip()

 
if __name__ == '__main__':

    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)