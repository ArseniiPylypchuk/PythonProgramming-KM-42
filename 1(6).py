phrase1= input("Введіть першу фразу:")
phrase2= input("Введіть другу фразу:")
print(phrase1)
print(phrase2)
set1 = {char.lower() for char in phrase1 if char.isalpha()}
set2 = {char.lower() for char in phrase2 if char.isalpha()}
x = set2&set1
if x:
    print("Можна скласти другу фразу з літер першої фрази.")
else:
    print("Не можна скласти другу фразу з літер першої фрази.")