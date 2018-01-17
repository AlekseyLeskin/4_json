import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as open_file:
        return json.load(open_file)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        user_filepath = load_data(input('Укажите путь до файла: '))
    else:
        user_filepath = load_data(sys.argv[1])
    pretty_print_json(user_filepath)
