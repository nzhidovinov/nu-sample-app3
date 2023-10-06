lst = []
n = int(input('Введите количество элементов: '))
for i in range(n):
    el = int(input(f'Введите {i + 1} элемент: '))
    lst.append(el)
print(f'Вывод: {sorted(lst)}')