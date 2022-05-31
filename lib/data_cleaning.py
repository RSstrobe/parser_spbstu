import re


def data_cleaning(lines):
    """
    Функция возвращает очищенный список с данными для парсинга.
    :param lines: lines from ECLIPSE document
    :return: clean list
    """

    list_first = []

    # Использование регулярных выражений для очистки данных
    for line in lines:
        line = re.sub(r'\t', ' ', line)
        line = re.sub(r'/', '', line)
        line = re.sub(r"'", '', line)
        line = line.split("--")[0]
        line = line.strip()
        line = re.sub(" +", " ", line)
        line = line.replace('1*', 'DEFAULT')
        line = line.replace('3*', 'DEFAULT DEFAULT DEFAULT')
        if line and line.strip():
            list_first.append(line)

    # Находим индексы с датами
    list_data = []
    for index, elem in enumerate(list_first):
        f = re.findall(r'[0-9][0-9]\s[A-Z]+\s[0-9]{4}', elem)
        if f:
            list_data.append(index)

    # Есди перед датой нет слова DATES, то ставим это слово
    for number in range(len(list_data) - 1):
        if list_data[number + 1] - list_data[number] == 1:
            list_first.insert(list_data[number + 1], 'DATES')

    # Алгоритм удаления WEFAC
    list_2 = list_first[:]
    indices = [i for i, x in enumerate(list_first) if x == "WEFAC"]
    for index in indices:
        list_for_drop = []
        i = index
        while list_first[i] not in ['DATES', 'COMPDAT', 'COMPDATL', 'END']:
            list_for_drop.append(i)
            i += 1
        del list_2[list_for_drop[0]:list_for_drop[-1] + 1]
    list_2 = list_2[:list_2.index('END')]
    # Ищем первое ключевое слово (Начало работы программы)
    start_list = []
    for start in ['DATES', 'COMPDAT', 'COMPDATL']:
        start_list.append(list_first.index(start))
    start_index = min(start_list)

    # Сепарация списка на сегменты
    list_final = []
    indices = [i for i, x in enumerate(list_2) if x == "DATES"]
    indices.insert(0, start_index)
    indices.append(len(list_2))
    for index in range(len(indices) - 1):
        list_final.append(list_2[indices[index]:indices[index + 1]])
    return list_final
