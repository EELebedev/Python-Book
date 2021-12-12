# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip, mask= input("please enter as '10.1.1.0/24': ").split("/")
ip = list(map(int, ip.split(".")))

print("Network:")
print(f"{ip[0]:<10}{ip[1]:<10}{ip[2]:<10}{ip[3]:<10}")
print(f"{ip[0]:08b}  {ip[1]:08b}  {ip[2]:08b}  {ip[3]:08b}")
print("Mask:")
print(f"/{mask}")

bin_mask = int(mask)*"1"+(32-int(mask))*"0"
bin_mask_first_oct = bin_mask[:8]
bin_mask_second_oct = bin_mask[8:16]
bin_mask_third_oct = bin_mask[16:24]
bin_mask_fourth_oct = bin_mask[24:]



print(f"{int(bin_mask_first_oct, 2):<10}{int(bin_mask_second_oct, 2):<10}{int(bin_mask_third_oct, 2):<10}{int(bin_mask_fourth_oct, 2):<10}")
print(f"{bin_mask_first_oct}  {bin_mask_second_oct}  {bin_mask_third_oct}  {bin_mask_fourth_oct}")