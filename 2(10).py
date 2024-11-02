import numpy as np
years =np.arange(1900, 2024,1)
def is_leap_year(year):
    return(year % 400 == 0) or (year% 100!= 0 and year% 4 ==0)
def leap_years_list(years):
    return list(filter(is_leap_year, years))
def days_in_month(leap_year_func, month, year):
    days_in_month_normal= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_in_month_leap= {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year_func(year):
        return days_in_month_leap.get(month, "Неправильний місяць")
    else:
        return days_in_month_normal.get(month, "Неправильний місяць")
leap_years= leap_years_list(years)
print("Високосні", leap_years)
try:
    month= int(input("(1-12)"))
    if month< 1 or month > 12:
        raise ValueError("Номер місяця має бути від 1 до 12.")
    year= int(input("Введіть рік"))
    if year<1000 or year > 9999:
        raise ValueError("Рік має бути чотирицифровим числом.")
    days= days_in_month(is_leap_year, month, year)
    print(month, year, days)
except ValueError as e:
    print("Помилка", e)
