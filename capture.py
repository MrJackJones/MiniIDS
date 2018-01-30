# -*- coding: utf-8 -*-
# Подключаем библотеки
from scapy.all import *
import sys
import os
import django

# Настраиваем подуль для подключения в Django
sys.path.append('ids_admin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ids_admin.settings'
django.setup()

# Подлючаем модель для записи данных
from main.models import Data

# Функция записи данных в таблицу БД
def custom_action(packet):
    data = Data.objects.create(ethernet_dst=packet.dst,
                       ethernet_src=packet.src,
                       ip_proto=packet.proto,
                       ip_dst=packet['IP'].dst,
                       ip_src=packet['IP'].src,
                       tcp_sport=packet['IP'].sport,
                       tcp_dport=packet['IP'].dport,
                       raw=packet.payload)
    data.save()
    return data


# Вызов в бесконечном цикле захвата пакетов
if __name__ == '__main__':
    while True:
        sniff(filter='ip', prn=custom_action)

