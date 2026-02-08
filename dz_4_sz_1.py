from datetime import datetime


def get_days_from_today(date):
    # 1. Перетворюємо рядок 'YYYY-MM-DD'
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Невірний формат, потрібно використовувати 'YYYY-MM-DD'")
        return None

    # 2. Отримуємо дату на сьогодні
    today = datetime.today().date()

    # 3. Розраховуємо різницю між поточною датою та заданою датою
    delta = today - target_date

    # 4. Повертаємо кількість днів
    return delta.days

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-08-02"))
print(get_days_from_today("2028/12/31"))
