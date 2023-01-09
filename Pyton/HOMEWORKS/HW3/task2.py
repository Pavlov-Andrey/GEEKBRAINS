# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
multi_num = []
for i in range((len(my_list) // 2 + len(my_list) % 2)):
    new_num = my_list[i] * my_list[-i - 1]
    multi_num.append(new_num)
print(f'произведение пар чисел: {multi_num}')

