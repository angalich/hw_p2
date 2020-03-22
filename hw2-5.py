my_list = [7, 5, 3, 3, 2]
new_elem = int(input("Enter new list element: "))
for el in range(len(my_list)):
    if my_list[el] == new_elem:
        my_list.insert(el, new_elem)
        break
    elif my_list[0] < new_elem:
        my_list.insert(0, new_elem)
    elif my_list[-1] > new_elem:
        my_list.append(new_elem)
    elif my_list[el] > new_elem and my_list[el + 1] < new_elem:
        my_list.insert(el + 1, new_elem)
print(my_list)
#+