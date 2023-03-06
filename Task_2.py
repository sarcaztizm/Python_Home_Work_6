# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума
# Ввод:
# [-5,9,0,3,-1,-2,1,4,-2,2,0,-9,8,10,-9,0,-5,-5,7]
# 5
# 15
# Вывод: [1,13,14,19]

from random import randint

print('Список элеметнов: ')
list_nums = [randint(1, 10) for i in range(randint(5,10))]
print(list_nums)
min = int(input('Заданный минимум: '))
max = int(input('Заданный максимум: '))

index_result = [i for i in range(len(list_nums))
                if min <= list_nums[i] <= max]

print(index_result)

