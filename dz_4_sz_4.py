from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        # 1. Дата народження як date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2. День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # 3. Якщо в цьому році вже минув, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4. Різниця в днях між сьогодні і днем народження
        delta_days = (birthday_this_year - today).days

        # 5. Цікавлять тільки дні від 0 до 7 включно
        if 0 <= delta_days <= 7:
            congratulate_date = birthday_this_year

            # 6. Якщо вихідний — переносимо на понеділок
            if congratulate_date.weekday() == 5:  # субота
                congratulate_date += timedelta(days=2)
            elif congratulate_date.weekday() == 6:  # неділя
                congratulate_date += timedelta(days=1)

            # 7. Додаємо в результат
            result.append({
                "name": user["name"],
                "congratulation_date": congratulate_date.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
