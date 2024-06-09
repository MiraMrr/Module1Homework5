immutable_var = (1, 2, 3, 'four', 'five', True)
print(immutable_var)

# immutable_var[0] = 'one'
# При попытке изменить значение элемента кортежа возникает следующая ошибка:
# TypeError: 'tuple' object does not support item assignment
# Это значит, что изменить значение элемента кортежа невозможно, т.к. кортеж не поддерживает обращение по элементам

mutable_list = ['one', 'two', 'three', 4, 5]
print(mutable_list)
mutable_list[0] = 1
mutable_list.append('six')
mutable_list.extend(['seven', False])
print(mutable_list)