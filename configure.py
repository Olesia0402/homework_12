from collections import UserDict
from datetime import date, datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    @property
    def check_value(self):
        return self.value

    @check_value.setter
    def check_value(self, new_value):
        if True:
            self.value = new_value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def check_phone(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError('Invalid phone number')
        return self.value


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def check_birthday(self):
        try:
            self.value = datetime.strptime(self.value, "%d/%m/%y").date()
            return self.value
        except ValueError:
            print(f'{self.value} have not correct format')


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
        self.current_day = date.today()

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return phone

    def remove_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return self.phones.remove(i)

    def edit_phone(self, phone: str, new_phone: str):
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return i.value
            else:
                raise ValueError('Phone is not in list')

    def find_phone(self, phone: str):
        for n, i in enumerate(self.phones):
            if str(i) == phone:
                return self.phones[n]

    def day_to_birthday(self):
        if self.birthday is None:
            return 'You did not enter the birthday to this contact.'
        self.birthday = Birthday(self.birthday)
        if Birthday(self.birthday) < self.current_day:
            self.birthday = self.birthday.replace(year=self.current_day.year+1)
        self.time_to_birthday = abs(self.birthday - self.current_day)
        return self.time_to_birthday.days


class AddressBook(UserDict):
    def iterator(self, step):
        self.count = 0
        self.step = step
        while self.count < len(self.data):
            yield self.data[self.count:self.count+self.step]
            self.count += self.step

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return self.data

    def find(self, name):
        for key, value in self.data.items():
            if key == name:
                return value

    def delete(self, name):
        for i in self.data.keys():
            if i == name:
                return self.data.pop(i)


if __name__ == '__main__':
    address_book = AddressBook()
