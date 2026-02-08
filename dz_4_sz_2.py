import random

def get_numbers_ticket(min, max, quantity):
    # діапазон вказуємо
    if min < 1 or max > 1000:
        return []
    
    # перевіряємо наш діапазон
    if quantity > (max - min + 1):
        return []
    
    # генеруємо випадков числа
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# min >= 1
# max <= 1000
# quantity (max - min + 1)