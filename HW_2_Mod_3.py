from collections import Counter, defaultdict

# class work
#<----------------------------------------->
# d = {3: 4, 15: 8, 13: 11, 8: 2}
# print (d)
# print (d.get(13))
# print (list(d.keys()))
# print (list(d.values()))

# HW:
# Задания:
# 1. Создать словарь, где ключи и значения числа
# 2. Посчитать сумму ключей, значений, всех абсолютно чисел
# 3. Вывести значения, где ключи - четные числа
# 4. Вывести самый большой ключ
# 5. Вывести значение пары с самым маленьким ключем
# 6. Удалить пару где ключ 3
# 7. Сгенерировать словарь:
#  {1:5, 2:4, 3:3, 4:2, 5:1}
#  {1:5, 2:4, 3:0, 4:2, 5:1}
# 8. Найти среднее значение всех ключей
# 9. Попробовать все методы множеств


# task 1
#<----------------------------------------->
# create dictionary
#d = {3: 4, 15: 8, 13: 11, 8: 2}


# task 2
#<----------------------------------------->
#d = {3: 4, 15: 8, 13: 11, 8: 2}


#keys sum
# ansk = 0
# for i in d.keys():
#     ansk = ansk + i
# print (ansk)


#val sum
# ansv = 0
# for i in d.values():
#     ansv = ansv + i
# print (ansv)


#all sum
# ansall = 0
# for i in (list(d.keys()) + list(d.values())):
#     ansall = ansall + i
# print (ansall)


#all sum alternative
# ansall = 0
# for k, v in d.items():
#     ansall = ansall + k + v
# print (ansall)


# task 3
#<----------------------------------------->
# d = {3: 4, 15: 8, 13: 11, 8: 2, 34: 5}
# for i in d.keys():
#     if i % 2 == 0:
#         print (i)


# task 4
#<----------------------------------------->
# d = {133: 4, 15: 8, 13: 11, 8: 2, 34: 5, 88: 5}
# j = list(d.keys())[0]
# for i in d.keys():
#     if i > j:
#         j = i
# print (j)


# task 5
#<----------------------------------------->
# d = {133: 4, 15: 8, 13: 11, 8: 2, 34: 5, 88: 5}
#
# j = list(d.keys())[0]
# for i in d.keys():
#     if i < j:
#         j = i
# print (str(j) + ':' + str(d.get(j)))


# task 6
#<----------------------------------------->
# d = {3: 4, 15: 8, 13: 11, 8: 2, 34: 5, 88: 5}
# j = d.pop(3)
# print(d)


# task 7
#<----------------------------------------->
# l = [i for i in range(1,6)]
#
# d = {} #defaultdict(int)
# d = Counter(l)
#
# # for i in l:
# #     d[i] += -1
#
#
# print (d)
