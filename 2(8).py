import math
try:
    a = int(input())
    b = int(input())
    c = int(input())
    disc= b**2-4*a*c
    x1=(-b+math.sqrt(disc))/(2*a)
    x2=(-b-math.sqrt(disc))/(2*a)
except ZeroDivisionError:
        print("Помилка: ділення на 0 або коефіцієнт 'a' не може дорівнювати 0.")
except NameError:
       print("Напишіть число")
except ValueError as e:
        print(e)
print(x1)
print(x2)
