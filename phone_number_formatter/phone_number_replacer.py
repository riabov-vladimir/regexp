from phone_number_formatter.phone_number_regexp import format_phone_number


def phone_number_replacer(contacts: list) -> list:

	for contact in contacts:
		print(contact[-2])
		contact[-2] = format_phone_number(contact[-2])
		print(contact[-2])

	return contacts

if __name__ == '__main__':
	numbers = [['+7 (495) 913-04-78', 0], ['+74959130037', 0], ['8 495-913-0168', 0], ['+7 (495) 983-36-99 доб.2926',
																					   0], ['8(495)748-49-73', 0],	['+7 (495) 913-11-11 (доб. 0792)', 0]]
	# print(numbers)
	# print(type(numbers))
	print(phone_number_replacer(numbers))
