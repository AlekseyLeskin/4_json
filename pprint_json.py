import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        filepath = load_data(input('Укажите путь до файла: '))
    else:
        filepath = load_data(sys.argv[1])
    pretty_print_json(filepath)
