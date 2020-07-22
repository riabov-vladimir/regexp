import re


def format_phone_number(phone_number: str) -> str:
	"""
	Форматирование телефонных номеров при помощи регулярного выражения
	:param phone_number:
	:return: phone_number в формате +7(999)999-99-99
	"""

	phone_regex = r"(\+?[+78])\s?\(?(\d{3})\)?[- ]?(\d{3})\-?(\d{2})\-?(\d{2})\s?((\(?(доб.)\s(\d+)\)?)?)"

	pattern = re.compile(phone_regex)

	if 'доб' in phone_number:
		phone_number_formatted = pattern.sub(r'+7(\2)\3-\4-\5 (доб. \9)', phone_number)
	else:
		phone_number_formatted = pattern.sub(r'+7(\2)\3-\4-\5', phone_number)

	return phone_number_formatted


if __name__ == '__main__':
	phone_number = '+7 (495) 913-1111'  # (доб. 0792)'
	print(format_phone_number(phone_number))
