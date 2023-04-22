import random
import pprint


# создание файла по умолчанию, если необходимо
def create_default_file() -> None:
    family_names = ["Драгунов", "Пушкевич", "Штурвалов"]
    personal_names = ["Павел", "Константин", "Илья"]

    # Открытие файла для перезаписи, если нет, то создаст. Безопасный способ
    with open('data.csv', 'w', newline='') as temp_file:
        # Комбинация фамилий с именами с последующей записью в файл
        for f in family_names:
            for p in personal_names:
                name_len = len(f) + len(p)
                false_len = name_len + random.randint(1, 5)  # сумма количества символов полного имени плюс рандом
                print(f, p, false_len, file=temp_file)  #  вывод в файл


# Создание списка строк
def load_data() -> list[str]:
    try:
        temp_file = open('data.csv', 'r')
    except FileNotFoundError:  # Если файла нет, он будет создан и прочитан
        create_default_file()
        temp_file = open('data.csv', 'r')

    asked_lines = temp_file.readlines()
    for i in range(len(asked_lines)):
        asked_lines[i] = asked_lines[i].rstrip()  # удаление \n в конце (справа)
    temp_file.close()
    return asked_lines


# Парсер для разбивки одной строки на "слова"
def parse(lines: list[str], sep: str ='Д') -> list[list[str]]:
    accounts: list[list[str]] = []  # сюда будет записаны отсортированные данные
    man: list[str] = []  # для отдельных "слов"
    for line in lines:
        word: str = ''  # для отдельных символов
        # Цикл посимвольного перебора строки и разбития на "слова". 
        for i in range(len(line)):
            if i == len(line) - 1:  # особая обработка для последнего символа
                if not (line[i].isspace()):
                    word += line[i]
                    man.append(word)
                    word = ''
            elif line[i].isspace():  # отлавливает пробел, \t, \n и т.д.
                man.append(word)
                word = ''
            else:
                word += line[i]
        accounts.append(man)
        man = []
    return accounts


create_default_file()  # создание файла
lines = load_data()  # считывание файла
accounts = parse(lines)  # парсинг данных из файла

# Добавление дивидендов
for man in accounts:
    o = int(man[-1])
    d = o * 50  # реализация формулы d = o * 1000 * 5%
    man.append(str(d))

# запись данных в новый файл
with open('data_updated.csv', 'w', newline='') as temp_file:
    for man in accounts:
        temp = ''
        for line in man:
            temp += line + ' '
        temp = temp.rstrip()  # убирает лишний пробел
        print(temp, file=temp_file)  # отправляет подготовленную строку в файл
