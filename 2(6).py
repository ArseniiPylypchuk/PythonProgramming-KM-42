provinces = {'A': "Newfoundland",
    'B': "Nova Scotia",
    'C': "Prince Edward Island",
    'E': "New Brunswick",
    'G': "Quebec",
    'H': "Quebec",
    'J': "Quebec",
    'K': "Ontario",
    'L': "Ontario",
    'M': "Ontario",
    'N': "Ontario",
    'P': "Ontario",
    'R': "Manitoba",
    'S': "Saskatchewan",
    'T': "Alberta",
    'V': "British Columbia",
    'X': "Nunavut",
    'X': "Northwest Territories",
    'Y': "Yukon"}
index = input("Введіть поштовий індекс:")
if len(index) != 3 or not index[0].isalpha() or not index[1].isdigit() or not index[2].isalpha():
    print("Помилка")
else:
    x = index[0].upper()
    y = index[1]
    j = index[2].upper()
    if x in provinces:
        province = provinces[x]
        if y == '0':
            miscevistb = "сільській"
        else:
            miscevistb = "міській"
        print(f"Адресат знаходиться у {miscevistb} місцевості провінції {province}.")
    else:
        print("Помилка: Неправильний перший символ поштового індекса.")
