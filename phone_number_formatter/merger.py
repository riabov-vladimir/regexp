def merge_contacts(contact_a: list, contact_b: list) -> list:
	"""
	Когда мы нашли контакты с одинаковой фамилией, передаём оба контакта
	данной функции в качестве аргументов, чтобы она вернула обновленный контакт с
	максимумом данных
	:param contact_a: list
	:param contact_b: list
	:return: list
	"""
	contact_merged = ['', '', '', '', '', '', '']

	for index in range(0, 7):
		if contact_a[index] == '':
			contact_merged[index] = contact_b[index]
		else:
			contact_merged[index] = contact_a[index]

	return contact_merged


if __name__ == '__main__':
	contact_b = ['Лагунцов', '', 'Алексеевич', 'Минфин', '', '+7(495)913-11-11 доб.0792', '']
	contact_a = ['', 'Иван', '', '', '', '', 'Ivan.Laguntcov@minfin.ru']

	a = merge_contacts(contact_a, contact_b)
	print(a)