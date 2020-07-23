from phone_number_formatter.phone_number_regexp import format_phone_number


def phone_number_replacer(contacts: list) -> list:

	for contact in contacts:

		contact[-2] = format_phone_number(contact[-2])

	return contacts
