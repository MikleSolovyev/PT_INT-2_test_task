# INT-2 test task
Тестовое задание в отдел INT-2
"Группа автоматизации соответствия стандартам безопасности" в рамках 2-го этапа стажировки
2023.2 PT-START Intensive.

Задание выполнено на основе данного [технического задания](https://sadykov.notion.site/INT-2-3a4e551dd9114b31a3778b337680b132).

## Built with
- [pydantic](https://github.com/pydantic/pydantic), [pydantic-settings](https://github.com/pydantic/pydantic-settings) -
библиотеки для декларативного описания моделей конфигурационного файла и сущности `Maxpatrol VM` (класс `Host`), а также
для валидации данных
- [pyyaml](https://github.com/yaml/pyyaml) - библиотека для парсинга yaml файлов
- [pytest](https://github.com/pytest-dev/pytest/) - библиотека для тестов
- [psycopg2](https://github.com/psycopg/psycopg2) - драйвер для postgresql
- [logging](https://docs.python.org/3/howto/logging.html) - встроенная библиотека для логирования
- [paramiko](https://github.com/paramiko/paramiko) - библиотека для реализации ssh в роли транспорта
- [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) - orm для базы данных
- [postgresql](https://www.postgresql.org/) - база данных

## Requirements
Скрипт тестировался на версиях Python 3.10+. Список необходимых зависимостей указан в файле `requirements.txt`.

## Getting Started
В папке `config` необходимо сконфигурировать файлы `config.yaml` и `profiles.json`.

В файле `config.yaml` находятся 4 поля конфигурации:
- `profiles` - отвечает за файл со сканируемыми профилями
- `ssh` - отвечает за выполняемые команды на удаленной машине
- `logger` - отвечает за настройки логгера
- `db` - отвечает за конфигурацию базы данных

Более подробные комментарии находятся внутри примера файла `config.yaml`.

Файл `profiles.json` представляет из себя json массив конфигураций подключения по ssh к каждой машине.
Каждый объект массива состоит из 4 полей:
- `ip` - IPv4 или IPv6 в формате строки
- `port` - строка из цифр либо число
- `username` - любая непустая строка
- `password` - любая строка

**Важно**: в файле `config.yaml` ключи словаря `commands` и значения словаря `columns`, а также вышеперечисленные поля в
файле `profiles.json` должны в точности (с учетом регистра) совпадать с соответствующими названиями атрибутов класса
`Host` в файле `src/host.py`. Это необходимо для корректного маппинга, поскольку скрипт построен вокруг класса `Host` 
(представляет из себя модель `Maxpatrol VM`), экземпляры которого передаются между всеми компонентами программы.

После конфигурирования скрипт можно **запустить** при помощи команды:
```bash
make
```
Таким образом можно запустить **тесты**:
```bash
make test
```
Вот так можно **очистить** созданные виртуальным окружением питона файлы и кэши:
```bash
make clean
```

## Additional Information
Так как это небольшой проект, который легко конфигурируется небольшим файлом настроек, было принято решение не реализовывать
графический интерфейс.

В папке `logs` находится файл `main.log` - пример файла лога, сконфигурированного настройками из файла `config.yaml`.

Таблица, на которой тестировалось добавление профилей машин в базу данных, была создана следующим SQL запросом:
```postgresql
create table profiles (
    id serial primary key,
    ip varchar not null,
    os_name varchar not null,
    os_ver varchar not null,
    os_arch varchar not null,
    created_at timestamptz default now()
)
```