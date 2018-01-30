#Mini IDS
## О программе
Простая IDS стистема на Python.

IDS работает следующим образом:
1) Трафик зеркалируется на IDS.
2) Весь полученный трафик записывается в базу данных DATA_SET.
3) Администратор через веб интерфейс формирует политики для распознавания зараженных устройств.
4) Система согласно политикам в случаи обнаружения вредоносных пакетов данных из таблицы DATA_SET выводит предупреждение на главной странице.

![alt text](https://preview.ibb.co/n2tOym/Screen_Shot_2018_01_30_at_12_57_29.png)
## Необходимое ПО и библиотеки:
1. Python 3.6
2. Django 2.0
3. PostgreSQL
4. scapy-python3
5. peewee

## Установка:
1. Копируем репозиторий:
```bash
git clone https://github.com/MrJackJones/Mini_IDS.git
```

2. Устанавливаем необходимые библиотеки:
```bash
pip3.6 install requirements.txt
```

3. Подготовливаем  базу:
```bash
python3.6 manage.py makemigrations
python3.6 manage.py migrate
```

4. Создаем главного администратора:
```bash
python3.6 manage.py createsuperuser
```

5. Запускаем сервер
```bash
python3.6 manage.py runserver
```

## Запуск захвата трафика 
```bash
python3.6 capture.py
```