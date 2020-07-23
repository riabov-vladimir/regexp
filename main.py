from phone_number_formatter.phone_number_replacer import phone_number_replacer
import csv
from pprint import pprint

with open("C:/Users/79055/PycharmProjects/regexp/data/phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_number_replacer(contacts_list)

new_contacts_list = []


for contact in contacts_list:
    if len(contact[0].split()) == 3:
        temp = contact[0].split()
        contact[0] = temp[0]
        contact[1] = temp[1]
        contact[2] = temp[2]
    elif len(contact[1].split()) == 2:
        temp = contact[1].split()
        contact[1] = temp[0]
        contact[2] = temp[1]
    elif len(contact[0].split()) == 2:
        temp = contact[0].split()
        contact[0] = temp[0]
        contact[1] = temp[1]

contacts_list1 = contacts_list.copy()

for contact in contacts_list1:
    contacts_list1.remove(contact)
    for y in contacts_list1:
        if y[0] == contact[0]:
            print(y[0], contact[0])
            print('---------------------------------------------------')