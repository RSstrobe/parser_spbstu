from lib.data_cleaning import data_cleaning
from lib.prepare_list_for_dataframe import prepare_list_for_dataframe
import pandas as pd


def parsing(filename):
    """
    Функция для парсинга документа ECLIPSE.
    :param filename: path of document
    :return: dataframe
    """
    columns_name = [
        'Date',
        'Well name',
        'Local grid name',
        'I',
        'J',
        'K upper',
        'K lower',
        'Flag on connection',
        'Saturation table',
        'Transmissibility factor',
        'Well bore diameter',
        'Effective Kh',
        'Skin factor',
        'D-factor',
        'Dir_well_penetrates_grid_block',
        'Press_eq_radius'
    ]

    # Чтение файла
    with open(filename, encoding='UTF-8') as f:
        lines_from_document = f.read().splitlines()

    # Очищенный список
    clean_list = data_cleaning(lines_from_document)

    # Готовим список для датафрейма
    list_for_df = prepare_list_for_dataframe(clean_list)

    # Создаем датафрейм
    final_df = pd.DataFrame(list_for_df, columns=columns_name)

    return final_df
