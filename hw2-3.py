seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца года: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif 3 >= month <= 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif 6 >= month <= 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif 9 >= month <= 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
#+