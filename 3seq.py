s = input('Введите элементы списка 1 через запятую: ')
lst1 = [int(l) for l in s.split(',')]
s = input('Введите элементы списка 2 через запятую: ')
lst2 = set([int(l) for l in s.split(',')])
res = []
for l1 in lst1:
    if l1 not in lst2:
        res.append(l1)
print('Результат: ', res)