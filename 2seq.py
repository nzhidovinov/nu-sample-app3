s = input('Введите элементы списка через запятую: ')
lst = [int(l) for l in s.split(',')]
lst = list(set(lst))
print('Результат: ', lst)