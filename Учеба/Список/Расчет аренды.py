initial_price = 9_000_000  # Начальная стоимость квартиры
initial_rent = 50_000      # Начальная стоимость аренды
rent_increase = 5_000      # Увеличение аренды
increase_interval = 2      # Интервал увеличения аренды (в годах)

total_earned = 0
years = 0
current_rent = initial_rent

while total_earned < initial_price:
    # Добавляем доход за год (аренда * 12 месяцев)
    total_earned += current_rent * 12
    years += 1
    
    # Проверяем, нужно ли увеличивать аренду (каждые 2 года)
    if years % increase_interval == 0:
        current_rent += rent_increase

print(f"Квартира окупится через {years} лет.")
print(f"Общий доход за это время: {total_earned} руб.")
print(f"Средняя стоимость аренды: {current_rent - rent_increase if years % increase_interval == 0 else current_rent} руб.")