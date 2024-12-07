import math

def Binomial_theorem(n):
    try: 
        for i in range(n +1):
            row= []
            for j in range(i+1):
                coefficient= math.factorial(i)// (math.factorial(j)*math.factorial(i-j))
                row.append(int(coefficient))
            yield row
    except ValueError:
        print("Ви ввели від'ємний коефіціент")
for row in Binomial_theorem(int(input("Введіть степінь многочлена"))):
    print(row)