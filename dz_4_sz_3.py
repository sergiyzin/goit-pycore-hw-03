import re

def normalize_phone(phone_number):
    #1 треба забрати зайві пробіли 
    phone_number = phone_number.strip()

    #2 видаляємо всі символи, що не є цифрами
    digits_only = re.sub(r"\D", "", phone_number)

    if digits_only.startswith("380"):
        normalized = "+" + digits_only
    else:
        normalized = "+38" + digits_only

    return normalized

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

