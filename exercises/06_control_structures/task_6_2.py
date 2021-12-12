# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Input ip (10.0.1.1): ")
ip = map(int, ip.split("."))

if 1<=ip[0]<=223:
    print("unicast")
elif 224<=ip[0]<=239:
    print("multicast")
elif ip[0]==255 and ip[1]==255 and ip[2]==255 and ip[3]==255:
    print("local broadcast")
elif ip[0]==0 and ip[1]==0 and ip[2]==0 and ip[3]==0:
    print("unassigned")
else:
    print("unused")