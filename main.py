from phone_number_formatter.phone_number_replacer import phone_number_replacer
import csv
from phone_number_formatter.merger import merge_contacts
from pprint import pprint

if __name__ == '__main__':

    with open("C:/Users/79055/PycharmProjects/regexp/data/phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    phone_number_replacer(contacts_list)  # форматируем все телефонные номера

    new_contacts_list = []  # здесь будем хранить повторяющиеся контакты в обобщенном виде

    for contact in contacts_list:   # здесь исправляем формат ФИО
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

    contacts_list1 = contacts_list.copy()  # копия изначального списка, для работы в нижестоящем цикле

    for contact1 in contacts_list1:  # поиск одинаковых контактов
        contacts_list1.remove(contact1)
        for contact2 in contacts_list1:
            if contact2[0] == contact1[0]:
                new_contacts_list.append(merge_contacts(contact1, contact2))  # объединение данных одинаковых контактов

    for contact_merged in new_contacts_list:  # удаление дублирующихся контактов из основного списка
        for contact in contacts_list.copy():
            if contact[0] == contact_merged[0]:
                contacts_list.remove(contact)

    contacts_list.extend(new_contacts_list)  # добавление обобщенных дублирующихся контактов в основной список

    with open("C:/Users/79055/PycharmProjects/regexp/data/phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list)

    pprint(contacts_list)
