def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")

def is_year_leap(year):
    return year % 4 == 0

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Вызываем функцию и сохраняем результат в переменную
year = 2024
year = 2015
year = 2028
year = 2009
result = is_year_leap(year)

# Выводим результат
print(f"год {year}: {result}")
