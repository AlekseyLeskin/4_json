# Prettify JSON

Программа принимает путь до файла с произвольными данными в формате JSON и выводит его содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Quickstart

* Склонировать этот репозиторий
* Запустить файл `pprint_json.py` либо в PyCharm, либо в командной строке:
```bash

$ python pprint_json.py

```
Будет предложено ввести путь до файла:
 ```bash
 
$ python pprint_json.py
Укажите путь до файла: 

```
 
Нужно указать путь до файла json и нажать 'Enter'. Пример результата работы скрипта:
```bash

$ python3 pprint_json.py
Укажите путь до файла: test.json
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    }
]

```

* Также есть возможность запустить скрипт из командной строки, сразу указав путь до файла. Пример:

 ```bash
 
$ python pprint_json.py test.json

```

При вводе несуществующего файла скрипт выдаст ошибку:

```bash

$ python3 pprint_json.py incorrect_file
Файла не существует

```
и прекратит работу.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
