my_line = input("Enter words in line: ")
for i, el in enumerate(my_line.split(), 1):
    print(f'{i} {el[:10]}')
#+