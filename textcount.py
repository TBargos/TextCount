import io
import random  # генератор псевдорандома


# создание файла по умолчанию, если необходимо
def create_default_file() -> None:
    family_names = ["Драгунов", "Пушкевич", "Штурвалов"]
    personal_names = ["Павел", "Константин", "Илья"]

    # Открытие файла для перезаписи, если нет, то создаст. Безопасный способ
    with open('data.csv', 'w', newline='') as temp_file:
        for f in family_names:
            for p in personal_names:
                name_len = len(f) + len(p)
                false_len = name_len + random.randint(1, 5)  # сумма количества символов полного имени плюс рандом
                print(f, p, false_len, file=temp_file)  #  вывод в файл


def load_data():
    temp_file: io.TextIOWrapper
    try:
        temp_file = open('data.csv', 'r')
    except FileNotFoundError:
        create_default_file()
        temp_file = open('data.csv', 'r')

    asked_lines = temp_file.readlines()
    for i in range(len(asked_lines)):
        asked_lines[i] = asked_lines[i].rstrip()
    return asked_lines


lines = load_data()
man = []
word = ''
for i in range(len(lines[0])):
    if lines[0][i].isspace() or i == len(lines[0]) - 1:
        man.append(word)
        word = ''
        continue
    else:
        word += lines[0][i]

print(man)