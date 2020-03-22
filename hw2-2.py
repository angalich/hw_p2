amount = int(input("Enter amount of elements in list: "))
my_list = []
i = 0
el = 0
while i < amount:
    my_list.append(input("Enter next number in list: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
#+