# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Input ip (10.0.1.1): ")
try:
    #check separator 
    if "." not in ip:
        raise Exception("WrongSeparator")

    ip = map(int, ip.split("."))

    #check ip length
    if len(ip)!=4:
        raise Exception("Wronglength")
    #check adress
    for oct in ip:
        if not 0<=oct<=255:
            raise Exception("WrongAdress")
            
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
except Exception:
    print("Неправильный IP-адрес")